from numpy.core.einsumfunc import _compute_size_by_dict
from qgis.PyQt.QtWidgets import QAction
from PyQt5.QtGui import QFont, QColor
from qgis.utils import iface
from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (
    Qgis,
    # QgsField,
    # QgsFields,
    # QgsWkbTypes,
    QgsExpression,
    QgsPointXY,
    QgsProject,
    QgsPrintLayout,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsUnitTypes,
    QgsTextFormat,
    QgsLayoutItemPage,
    QgsLayoutItemMap,
    QgsLayoutItemLabel,
    QgsLayoutMeasurement,
    QgsLayoutItemScaleBar,
    QgsMapSettings,
    # QgsMapRendererParallelJob,
    QgsLayoutExporter,
    # QgsFeature,
    QgsGeometry,
    QgsRectangle,
    QgsProcessing,
    QgsFeatureSink,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer,
)

import numpy as np

# FIXME: this hardcoded stuff should be dynamic
THEMES_NAMES = ["landeskarte", "1984", "1996", "2002", "2008", "2014", "2020"]
MARGIN = np.array([20, 20])  # (x,y)
INTER_MARGIN = np.array([20, 20])  # (x,y)
LAYOUT_MDIM = np.array([3, 3])  # (nrow, ncol)
MAP_ITEM_SIZE = np.array(
    [50, 50]
)  # the size of the map items in mm in (x,y) dimensions


class AreappPrintLayout:
    def __init__(self):
        # gets a reference to the project instance
        self.project = QgsProject.instance()
        # gets a reference to the layout manager
        self.manager = self.project.layoutManager()
        # get reference to tree root
        self.root = self.project.layerTreeRoot()
        # reference to all layers
        self.layers = self.project.mapLayers()

        self.title = "Areapp print POC"
        self.layoutName = "testAreapp"
        self.pageSize = "A4"

        self.reset()

    def reset(self):
        # delete and create again the layout if already exists
        layouts_list = self.manager.printLayouts()
        for layout in layouts_list:
            if layout.name() == self.layoutName:
                self.manager.removeLayout(layout)
        self.layout = QgsPrintLayout(self.project)
        self.layout.initializeDefaults()
        self.layout.setName(self.layoutName)

        self.layout.pageCollection().page(0).setPageSize(
            self.pageSize, QgsLayoutItemPage.Landscape
        )
        self.manager.addLayout(self.layout)

    @staticmethod
    def computeMapLayoutItemPosition(
        mapItemSize: np.array,  # (dx, dy)
        margin: np.array,  # (m_x, m_y)
        inter_margin: np.array,  # (im_x, im_y)
        index: np.array,  # matrix index of the item to display (r, c)
    ):
        return np.array(
            [
                margin[0] + index[1] * (mapItemSize[0] + inter_margin[0]),
                margin[1] + index[0] * (mapItemSize[1] + inter_margin[1]),
            ]
        )

    def print(self, filename: str, center: QgsPointXY, scale: float):
        self.reset()

        # FIXME: to be flexible on paper size, we should base the computing of dimension on these 2 variables:
        # self.layout.pageCollection().page(0).pageSize().width()
        # self.layout.pageCollection().page(0).pageSize().height()

        label = QgsLayoutItemLabel(self.layout)
        label.setText(self.title)
        label.setFont(QFont("Arial Black", 16))
        label.adjustSizeToText()
        self.layout.addLayoutItem(label)
        layoutPosition = self.computeMapLayoutItemPosition(
            MAP_ITEM_SIZE, MARGIN, INTER_MARGIN, np.array([0, 0])
        )
        label.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1],
                QgsUnitTypes.LayoutMillimeters,
            )
        )
        label.setLocked(True)

        # iterate over themes in the map matrix
        # applyTheme(self, name: str, root: QgsLayerTreeGroup, model: QgsLayerTreeModel)

        mapThemesCollection = QgsProject.instance().mapThemeCollection()
        mapThemesList = mapThemesCollection.mapThemes()

        layoutSubgrids = np.empty(LAYOUT_MDIM[0] * LAYOUT_MDIM[1], QgsLayoutItemMap)

        c = 1
        for name in THEMES_NAMES:
            c += 1
            layoutSubgrids[c] = name
        layoutSubgrids = layoutSubgrids.reshape(LAYOUT_MDIM)

        lCounter = 0
        for gridPosition in np.argwhere(layoutSubgrids):
            layoutPosition = self.computeMapLayoutItemPosition(
                MAP_ITEM_SIZE, MARGIN, INTER_MARGIN, gridPosition
            )
            map = QgsLayoutItemMap(self.layout)
            map.setId(THEMES_NAMES[lCounter])
            map.attemptMove(
                QgsLayoutPoint(
                    layoutPosition[0], layoutPosition[1], QgsUnitTypes.LayoutMillimeters
                )
            )
            map.attemptResize(
                QgsLayoutSize(
                    MAP_ITEM_SIZE[0], MAP_ITEM_SIZE[1], QgsUnitTypes.LayoutMillimeters
                )
            )
            bboxSize = MAP_ITEM_SIZE * scale
            x1 = center.x() - 0.5 * bboxSize[0]
            y1 = center.y() - 0.5 * bboxSize[1]
            x2 = center.x() + 0.5 * bboxSize[0]
            y2 = center.y() + 0.5 * bboxSize[1]
            map.setExtent(QgsRectangle(x1, y1, x2, y2))
            map.setScale(scale)
            map.setFollowVisibilityPreset(True)
            map.setFollowVisibilityPresetName(THEMES_NAMES[lCounter])
            # iface.mapCanvas().setTheme(THEMES_NAMES[lCounter])

            self.layout.addLayoutItem(map)

            lCounter += 1

        exporter = QgsLayoutExporter(self.layout)
        exporter.exportToPdf(filename, QgsLayoutExporter.PdfExportSettings())
