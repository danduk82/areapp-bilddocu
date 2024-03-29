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

import subprocess, os, platform


# FIXME: this hardcoded stuff should be dynamic

# self.margin = np.array([20, 20])  # (x,y)
# self.inter_margin = np.array([5, 5])  # (x,y)
# self.layoutMdim = np.array([3, 3])  # (nrow, ncol)
# self.mapItemSize = np.array(
#     [75, 60]
# )  # the size of the map items in mm in (x,y) dimensions


class AreappPrintLayoutBase:
    def __init__(self):
        # gets a reference to the project instance
        self.project = QgsProject.instance()
        # gets a reference to the layout manager
        self.manager = self.project.layoutManager()
        # get reference to tree root
        self.root = self.project.layerTreeRoot()
        # reference to all layers
        self.layers = self.project.mapLayers()


class AreappPrintLayoutPrinter(AreappPrintLayoutBase):
    def __init__(
        self,
        printLayoutName="default_template",
        necessaryThemes={"main": "landeskarte"},
        textItems={
            "commune": "comune name",
            "swissname": "swiss name",
            "class_de": "string in german",
            "class_fr": "string in french",
        },
        center=QgsPointXY(),
        scale=10000,
    ):
        super(AreappPrintLayoutPrinter, self).__init__()
        self.necessaryThemes = necessaryThemes
        self.scale = scale
        self.center = center
        self.textItems = textItems
        self.layoutTemplate = self.manager.layoutByName(printLayoutName)
        self.printLayout = self.layoutTemplate.clone()
        self.CreateItemsDict()
        self.UpdateMapItems()
        self.UpdateLabelItems()
        self.UpdateScaleBar()

    def CreateItemsDict(self):
        self.itemsDict = {}
        for item in self.printLayout.items():
            try:
                self.itemsDict[item.id()] = item
            except AttributeError:
                pass

    def GetItemById(self, itemId):
        for item in self.printLayout.items():
            try:
                if itemId == item.id():
                    return item
            except AttributeError:
                pass

    @staticmethod
    def SetMapItem(map, center, scale):
        bboxSize = (
            np.array([map.sizeWithUnits().width(), map.sizeWithUnits().height()])
            * scale
        )
        x1 = center.x() - 0.5 * bboxSize[0]
        y1 = center.y() - 0.5 * bboxSize[1]
        x2 = center.x() + 0.5 * bboxSize[0]
        y2 = center.y() + 0.5 * bboxSize[1]
        map.setExtent(QgsRectangle(x1, y1, x2, y2))
        map.setScale(scale)

    def UpdateMapItems(self):
        for key, value in self.necessaryThemes.items():
            try:
                self.SetMapItem(self.itemsDict[f"map_{key}"], self.center, self.scale)
            except KeyError:
                # silently pass over template items that do not exist
                pass

    def UpdateLabelItems(self):
        for key, value in self.necessaryThemes.items():
            try:
                self.itemsDict[f"label_{key}"].setText(str(value))
                self.itemsDict[f"label_{key}"].adjustSizeToText()
            except KeyError:
                # silently pass over template items that do not exist
                pass
        try:
            self.itemsDict[f"label_commune"].setText(str(self.textItems["commune"]))
            self.itemsDict[f"label_commune"].adjustSizeToText()
        except KeyError:
            pass
        try:
            coordinatesStr = "{:.2f}:{:.2f}".format(self.center.x(), self.center.y())
            self.itemsDict[f"label_coordinates"].setText(coordinatesStr)
            self.itemsDict[f"label_coordinates"].adjustSizeToText()
        except KeyError:
            pass
        try:
            self.itemsDict[f"label_swissname"].setText(str(self.textItems["swissname"]))
            self.itemsDict[f"label_swissname"].adjustSizeToText()
        except KeyError:
            pass
        try:
            self.itemsDict[f"label_class_de"].setText(str(self.textItems["class_de"]))
            self.itemsDict[f"label_class_de"].adjustSizeToText()
        except KeyError:
            pass
        try:
            self.itemsDict[f"label_class_fr"].setText(str(self.textItems["class_fr"]))
            self.itemsDict[f"label_class_fr"].adjustSizeToText()
        except KeyError:
            pass

    def UpdateScaleBar(self):
        try:
            scalebar = self.itemsDict[f"scalebar"]
            scalebar.setUnitsPerSegment(self.scale / 100)
            scalebar.update()
        except KeyError:
            # silently pass over template items that do not exist
            pass

    def print(self, filename: str = "/tmp/print.pdf"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        exporter = QgsLayoutExporter(self.printLayout)
        exporter.exportToPdf(filename, QgsLayoutExporter.PdfExportSettings())

        # also open the PDF directly for visualization
        if platform.system() == "Darwin":  # macOS
            subprocess.call(("open", filename))
        elif platform.system() == "Windows":  # Windows
            os.startfile(filename)
        else:  # linux variants
            subprocess.call(("xdg-open", filename))


class AreappPrintLayoutCreator(AreappPrintLayoutBase):
    def __init__(
        self,
        layoutName="default_template",
        necessaryThemes={"main": "landeskarte"},
        layoutMdim=np.array([3, 3]),  # (nrow, ncol)
        inter_margin=np.array([5, 5]),  # (x,y)
        margin=np.array([5, 5]),  # (x,y)
    ):
        super(AreappPrintLayoutCreator, self).__init__()

        self.title = "TITLE"
        self.layoutName = layoutName
        self.themesNames = [k for k in necessaryThemes.keys()]
        self.pageSize = "A4"
        self.layoutMdim = layoutMdim + np.array(
            [1, 0]
        )  # we add one free line for text etc
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
        self.ComputeMapItemSize()
        self.manager.addLayout(self.layout)

    def ComputeMapItemSize(self):
        sizeXY = np.array(
            [
                self.layout.pageCollection().page(0).pageSize().width(),
                self.layout.pageCollection().page(0).pageSize().height(),
            ]
        )

        # the size of the map items in mm in (x,y) dimensions
        self.mapItemSize = np.array([0, 0])
        self.mapItemSize[0] = (sizeXY[0] - 2 * self.margin[0]) / self.layoutMdim[
            1
        ] - self.inter_margin[0]
        self.mapItemSize[1] = (sizeXY[1] - 2 * self.margin[1]) / self.layoutMdim[
            0
        ] - self.inter_margin[1]

    @staticmethod
    def computeMapLayoutItemPosition(
        mapItemSize: np.array,  # (dx, dy)
        margin: np.array,  # (m_x, m_y)
        inter_margin: np.array,  # (im_x, im_y)
        index: np.array,  # matrix index of the item to display (row, col)
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

        layoutSubgrids = np.empty(
            self.layoutMdim[0] * self.layoutMdim[1], QgsLayoutItemMap
        )

        c = self.layoutMdim[1]
        for name in self.themesNames:
            layoutSubgrids[c] = name
            c += 1
        layoutSubgrids = layoutSubgrids.reshape(self.layoutMdim)

        lCounter = 0
        for gridPosition in np.argwhere(layoutSubgrids):
            layoutPosition = self.computeMapLayoutItemPosition(
                self.mapItemSize, self.margin, self.inter_margin, gridPosition
            )
            map = QgsLayoutItemMap(self.layout)
            map.setId(f"map_{self.themesNames[lCounter]}")
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
            label.setText(f"label_{self.themesNames[lCounter]}")
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

        label_commune = QgsLayoutItemLabel(self.layout)
        label_commune.setText("label_commune")
        label_commune.setId("label_commune")
        label_commune.setFont(QFont("Arial", 12))
        label_commune.adjustSizeToText()
        self.layout.addLayoutItem(label_commune)
        layoutPosition = self.computeMapLayoutItemPosition(
            self.mapItemSize, self.margin, self.inter_margin, np.array([0, 0])
        )
        label_commune.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1] + 20,
                QgsUnitTypes.LayoutMillimeters,
            )
        )

        label_swissname = QgsLayoutItemLabel(self.layout)
        label_swissname.setText("label_swissname")
        label_swissname.setId("label_swissname")
        label_swissname.setFont(QFont("Arial", 12))
        label_swissname.adjustSizeToText()
        self.layout.addLayoutItem(label_swissname)
        layoutPosition = self.computeMapLayoutItemPosition(
            self.mapItemSize, self.margin, self.inter_margin, np.array([0, 0])
        )
        label_swissname.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1] + 30,
                QgsUnitTypes.LayoutMillimeters,
            )
        )

        label_class_de = QgsLayoutItemLabel(self.layout)
        label_class_de.setText("label_class_de")
        label_class_de.setId("label_class_de")
        label_class_de.setFont(QFont("Arial", 12))
        label_class_de.adjustSizeToText()
        self.layout.addLayoutItem(label_class_de)
        layoutPosition = self.computeMapLayoutItemPosition(
            self.mapItemSize, self.margin, self.inter_margin, np.array([0, 1])
        )
        label_class_de.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1] + 20,
                QgsUnitTypes.LayoutMillimeters,
            )
        )

        label_class_fr = QgsLayoutItemLabel(self.layout)
        label_class_fr.setText("label_class_fr")
        label_class_fr.setId("label_class_fr")
        label_class_fr.setFont(QFont("Arial", 12))
        label_class_fr.adjustSizeToText()
        self.layout.addLayoutItem(label_class_fr)
        layoutPosition = self.computeMapLayoutItemPosition(
            self.mapItemSize, self.margin, self.inter_margin, np.array([0, 1])
        )
        label_class_fr.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1] + 40,
                QgsUnitTypes.LayoutMillimeters,
            )
        )
        label_coordinates = QgsLayoutItemLabel(self.layout)
        label_coordinates.setText("label_coordinates")
        label_coordinates.setId("label_coordinates")
        label_coordinates.setFont(QFont("Arial", 12))
        label_coordinates.adjustSizeToText()
        self.layout.addLayoutItem(label_coordinates)
        layoutPosition = self.computeMapLayoutItemPosition(
            self.mapItemSize, self.margin, self.inter_margin, np.array([0, 1])
        )
        label_coordinates.attemptMove(
            QgsLayoutPoint(
                layoutPosition[0],
                layoutPosition[1],
                QgsUnitTypes.LayoutMillimeters,
            )
        )
        scalebar = QgsLayoutItemScaleBar(self.layout)
        scalebar.setStyle("Line Ticks Up")
        scalebar.setId("scalebar")
        scalebar.setUnits(QgsUnitTypes.DistanceMeters)
        scalebar.setNumberOfSegments(4)
        scalebar.setNumberOfSegmentsLeft(0)
        # scalebar.setUnitsPerSegment(scale / 100)
        scalebar.setLinkedMap(map)
        scalebar.setUnitLabel("m")
        scalebar.setFont(QFont("Arial", 12))
        scalebar.update()
        self.layout.addLayoutItem(scalebar)
        scalebar.attemptMove(
            QgsLayoutPoint(
                self.margin[0],
                self.mapItemSize[1] - self.inter_margin[1],
                QgsUnitTypes.LayoutMillimeters,
            )
        )
