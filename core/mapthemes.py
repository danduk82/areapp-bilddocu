from typing import Dict
from numpy.core.einsumfunc import _compute_size_by_dict
from qgis.PyQt.QtWidgets import QAction
from PyQt5.QtGui import QFont, QColor
from qgis.utils import iface
from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.gui import QgsMapCanvas
from qgis.core import (
    Qgis,
    # QgsField,
    # QgsFields,
    # QgsWkbTypes,
    QgsExpression,
    QgsMapThemeCollection,
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
    QgsLayerTreeGroup,
    QgsLayerTreeLayer,
)

import numpy as np


class AreappMapThemes:
    def __init__(self, imagesAttributes, themesMapping) -> None:
        self.mapThemesCollection = QgsProject.instance().mapThemeCollection()

        # create a maping between period:year
        self.DefineThemesFromPointAttributes(imagesAttributes)
        # create the themes
        self.CreateThemes()
        # adapt the GUI, add canvases
        self.AddMapCanvasesIfNeeded()

        # load the theme and change the current displayed layer
        self.UpdateThemes(themesMapping)

        # after all reload the main theme with landeskarte on the main window

    def DefineThemesFromPointAttributes(self, imagesAttributes):
        self.necessaryThemes = {"main": "landeskarte"}  # reset
        if type(imagesAttributes) == type([]):
            for image in imagesAttributes:
                image = image.to_dict()
                try:
                    self.necessaryThemes[str("period_" + str(image["period"]))] = image[
                        "year"
                    ]
                except KeyError as e:
                    print(f"got a KeyError while parsing image: {e}")

    def AddMapCanvasesIfNeeded(self):
        # TODO: sync with main view!!!!
        mapCanvasesThemes = []
        iface.mapCanvas().setTheme("main")
        for mapCanvas in iface.mapCanvases():
            mapCanvasesThemes.append(mapCanvas.theme())
        mapCanvasesThemes.remove("main")
        try:
            mapCanvasesThemes.remove("")
        except ValueError:
            pass

        allThemes = list(self.necessaryThemes.keys())
        allThemes.remove("main")
        try:
            allThemes.remove("")
        except ValueError:
            pass
        toDo = list(set(mapCanvasesThemes).symmetric_difference(set(allThemes)))

        for theme in toDo:
            mp = iface.createNewMapCanvas(theme)
            if mp:
                mp.setTheme(theme)

    def CreateThemes(self):
        for map_theme_name in sorted(self.necessaryThemes.keys()):
            if not self.mapThemesCollection.hasMapTheme(map_theme_name):
                new_map_theme = self.mapThemesCollection.createThemeFromCurrentState(
                    QgsProject.instance().layerTreeRoot(), iface.layerTreeView().model()
                )
                # For QGIS 3.18+, instead of above line, use iface.layerTreeView().layerTreeModel()
                self.mapThemesCollection.insert(map_theme_name, new_map_theme)

    def UpdateThemes(self, themesMapping):
        root = QgsProject.instance().layerTreeRoot()
        mapThemes = self.mapThemesCollection.mapThemes()
        for themeName, year in themesMapping.items():
            if not self.mapThemesCollection.hasMapTheme(themeName):
                self.CreateThemes()
            visibleLayers = self.mapThemesCollection.mapThemeVisibleLayers(themeName)
            visibleLayer = visibleLayers[0] if len(visibleLayers) > 0 else None
            layer = QgsProject.instance().mapLayersByName(str(year))[0]
            print(f"visibleLayer = {visibleLayer}")
            print(f"layer = {layer}")
            if not visibleLayer or not visibleLayer.name() == layer.name():
                for child in root.children():
                    if isinstance(child, QgsLayerTreeLayer):
                        # print("- layer: " + child.name() + "  ID: " + child.layerId())
                        if child.name() == layer.name():
                            # check the correct layer
                            child.setItemVisibilityChecked(True)
                            print(f"Check {child.name()}")
                        else:
                            # uncheck the others
                            child.setItemVisibilityChecked(False)
                # update theme
                mapThemeState = self.mapThemesCollection.mapThemeState(themeName)
                mapThemeState.removeLayerRecord(visibleLayer)
                layerRecord = QgsMapThemeCollection.MapThemeLayerRecord(layer)
                mapThemeState.addLayerRecord(layerRecord)

                self.mapThemesCollection.update(themeName, mapThemeState)
                # find mapcanvas with that theme
                for mapCanvas in iface.mapCanvases():
                    if mapCanvas.theme() == themeName:
                        print("in mapcanvas")
                        mapCanvas.setTheme(None)
                        mapCanvas.setTheme(themeName)
                        mapCanvas.refresh()
