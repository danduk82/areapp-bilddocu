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
    QgsProcessingParameterExpression,
    QgsProcessingParameterString,
    QgsProcessingParameterNumber,
    QgsProcessingParameterEnum,
    QgsProcessingParameterExtent,
    QgsProcessingParameterMultipleLayers,
    QgsProcessingException,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterFileDestination,
)

from qgis import processing
import math

import os
import inspect
from qgis.PyQt.QtGui import QIcon


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

    def print(self, filename):
        self.reset()
        col_num = 3
        row_num = 2
        borderSize = 20  # border in mm
        xm = (
            self.layout.pageCollection().page(0).pageSize().width() - 2 * borderSize
        ) / col_num
        ym = (
            self.layout.pageCollection().page(0).pageSize().height() - 2 * borderSize
        ) / row_num

        nc = 0
        nl = 0
        # for canvas in self.iface.mapCanvases():

        label = QgsLayoutItemLabel(self.layout)
        label.setText(self.title)
        label.setFont(QFont("Arial Black", 18))
        label.adjustSizeToText()
        self.layout.addLayoutItem(label)
        label.attemptMove(
            QgsLayoutPoint(borderSize, borderSize - 10, QgsUnitTypes.LayoutMillimeters)
        )
        label.setLocked(True)
        exporter = QgsLayoutExporter(self.layout)
        exporter.exportToPdf(filename, QgsLayoutExporter.PdfExportSettings())
