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
    QgsSettings,
    QgsFeatureSink,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer,
)

import numpy as np

# FIXME: this hardcoded stuff should be dynamic

# self.margin = np.array([20, 20])  # (x,y)
# self.inter_margin = np.array([5, 5])  # (x,y)
# self.layoutMdim = np.array([3, 3])  # (nrow, ncol)
# self.mapItemSize = np.array(
#     [75, 60]
# )  # the size of the map items in mm in (x,y) dimensions


class AreappPrintLayout:
    def __init__(
        self,
        layoutName="default_template",
        necessaryThemes={"main": "landeskarte"},
        layoutMdim=np.array([3, 3]),  # (nrow, ncol)
        inter_margin=np.array([5, 5]),  # (x,y)
        margin=np.array([20, 20]),  # (x,y)
    ):
        # gets a reference to the project instance
        self.project = QgsProject.instance()
        # gets a reference to the layout manager
        self.manager = self.project.layoutManager()
        # get reference to tree root
        self.root = self.project.layerTreeRoot()
        # reference to all layers
        self.layers = self.project.mapLayers()

        self.title = "TITLE"
        self.layoutName = layoutName
        self.themesNames = [k for k in necessaryThemes.keys()]
        self.pageSize = "A4"
        self.layoutMdim = layoutMdim
        self.inter_margin = inter_margin
        self.margin = margin

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
        self.ComputeMapItemSize()

    def ComputeMapItemSize(self):
        sizeX = self.layout.pageCollection().page(0).pageSize().width()
        sizeY = self.layout.pageCollection().page(0).pageSize().height()

        self.mapItemSize = np.array(
            [75, 60]
        )  # the size of the map items in mm in (x,y) dimensions

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

    # center: QgsPointXY, scale: float
    def createLayout(self):
        self.reset()

        # FIXME: to be flexible on paper size, we should base the computing of dimension on these 2 variables:

        label = QgsLayoutItemLabel(self.layout)
        label.setText(self.title)
        label.setFont(QFont("Arial Black", 16))
        label.adjustSizeToText()
        self.layout.addLayoutItem(label)
        layoutPosition = self.computeMapLayoutItemPosition(
            self.mapItemSize, self.margin, self.inter_margin, np.array([0, 0])
        )
        label.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1],
                QgsUnitTypes.LayoutMillimeters,
            )
        )

        # FIXME: should use this generated somehow intelligently instead of self.themesNames
        # mapThemesCollection = QgsProject.instance().mapThemeCollection()
        # mapThemesList = mapThemesCollection.mapThemes()

        layoutSubgrids = np.empty(
            self.layoutMdim[0] * self.layoutMdim[1], QgsLayoutItemMap
        )

        c = 1
        for name in self.themesNames:
            c += 1
            layoutSubgrids[c] = name
        layoutSubgrids = layoutSubgrids.reshape(self.layoutMdim)

        lCounter = 0
        for gridPosition in np.argwhere(layoutSubgrids):
            layoutPosition = self.computeMapLayoutItemPosition(
                self.mapItemSize, self.margin, self.inter_margin, gridPosition
            )
            map = QgsLayoutItemMap(self.layout)
            map.setId(f"{self.themesNames[lCounter]}")
            map.attemptMove(
                QgsLayoutPoint(
                    layoutPosition[0], layoutPosition[1], QgsUnitTypes.LayoutMillimeters
                )
            )
            map.attemptResize(
                QgsLayoutSize(
                    self.mapItemSize[0],
                    self.mapItemSize[1],
                    QgsUnitTypes.LayoutMillimeters,
                )
            )

            map.setFollowVisibilityPreset(True)
            map.setFollowVisibilityPresetName(self.themesNames[lCounter])

            self.layout.addLayoutItem(map)

            label = QgsLayoutItemLabel(self.layout)
            label.setText(map.id())
            label.setId(f"label_{self.themesNames[lCounter]}")
            label.setFont(QFont("Arial Black", 12))
            label.adjustSizeToText()
            label.attemptMove(
                QgsLayoutPoint(
                    layoutPosition[0],
                    layoutPosition[1] - 5,  # FIXME: hardcoded
                    QgsUnitTypes.LayoutMillimeters,
                )
            )
            self.layout.addLayoutItem(label)
            lCounter += 1

        scalebar = QgsLayoutItemScaleBar(self.layout)
        scalebar.setStyle("Line Ticks Up")
        scalebar.setUnits(QgsUnitTypes.DistanceMeters)
        scalebar.setNumberOfSegments(4)
        scalebar.setNumberOfSegmentsLeft(0)
        # scalebar.setUnitsPerSegment(scale / 100)
        scalebar.setLinkedMap(map)
        scalebar.setUnitLabel("m")
        scalebar.setFont(QFont("Arial", 12))
        scalebar.update()
        self.layout.addLayoutItem(scalebar)
        scalebar.attemptMove(QgsLayoutPoint(20, 60, QgsUnitTypes.LayoutMillimeters))

    def CreatePrintTemplate(self, center, scale):
        bboxSize = self.mapItemSize * scale
        x1 = center.x() - 0.5 * bboxSize[0]
        y1 = center.y() - 0.5 * bboxSize[1]
        x2 = center.x() + 0.5 * bboxSize[0]
        y2 = center.y() + 0.5 * bboxSize[1]
        map.setExtent(QgsRectangle(x1, y1, x2, y2))
        map.setScale(scale)

    def print(self, filename: str = "/tmp/print.pdf"):
        exporter = QgsLayoutExporter(self.layout)
        exporter.exportToPdf(filename, QgsLayoutExporter.PdfExportSettings())
