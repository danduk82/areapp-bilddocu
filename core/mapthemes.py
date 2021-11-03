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

# root = QgsProject.instance().layerTreeRoot()

# mapThemesCollection = QgsProject.instance().mapThemeCollection()
# mapThemes = mapThemesCollection.mapThemes()
# # Where you need to set your images names
# # Could be retrieve if only raster names wanted with
# # [layer.name() for layer in QgsProject.instance().mapLayers().values() if isinstance(layer, QgsRasterLayer)]
# # If you want all layers names and filter them manually
# # [layer.name() for layer in QgsProject.instance().mapLayers().values()]
# layersToChanges = [
#     "CartoDB Light",
#     "OpenStreetMap",
#     "OpenTransports",
# ]  # Replace with your list of raster layers instead


# for layer in layersToChanges:
#     for child in root.children():
#         if isinstance(child, QgsLayerTreeGroup):
#             print("- group: " + child.name())
#         elif isinstance(child, QgsLayerTreeLayer):
#             print("- layer: " + child.name() + "  ID: " + child.layerId())
#             # Layer you want to tick
#             if child.name() == layer:
#                 child.setItemVisibilityChecked(True)
#                 print("Check only once")
#             elif child.name() in layersToChanges:
#                 child.setItemVisibilityChecked(False)
#                 print("Check the others you want to hide")
#     mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
#         QgsProject.instance().layerTreeRoot(),
#         iface.layerTreeView().model()
#         # For QGIS 3.18+, instead of above line, use iface.layerTreeView().layerTreeModel()
#     )
#     mapThemesCollection.insert(layer, mapThemeRecord)


class AreappMapThemes:
    def __init__(self, imagesAttributes) -> None:
        self.mapThemesCollection = QgsProject.instance().mapThemeCollection()

        # create a maping between period:year
        self.DefineThemesFromPointAttributes(imagesAttributes)
        # create the themes
        self.CreateThemes()
        # adapt the GUI, add canvases
        self.AddMapCanvasesIfNeeded()

        self.UpdateThemes()

        # load the theme and change the current displayed layer

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

        # todo, add the correct setLayers
        # https://qgis.org/pyqgis/3.2/gui/Map/QgsMapCanvas.html#qgis.gui.QgsMapCanvas.setLayers

    def CreateThemes(self):
        for map_theme_name in sorted(self.necessaryThemes.keys()):
            if not self.mapThemesCollection.hasMapTheme(map_theme_name):
                new_map_theme = self.mapThemesCollection.createThemeFromCurrentState(
                    QgsProject.instance().layerTreeRoot(), iface.layerTreeView().model()
                )
                self.mapThemesCollection.insert(map_theme_name, new_map_theme)

    def UpdateThemes(self, themesMapping):
        root = QgsProject.instance().layerTreeRoot()
        mapThemes = self.mapThemesCollection.mapThemes()$
        for themeName, year in themesMapping:
            if not self.mapThemesCollection.hasMapTheme(themeName):
                self.CreateThemes()
            visibleLayer = self.mapThemesCollection.mapThemeVisibleLayers(themeName)
            layer = QgsProject.instance().mapLayersByName(str(year))[0]
            if not visibleLayer.name() == layer.name():
                # update theme

                # find mapcanvas with that theme
                # reset theme on mapcanvas




# root = QgsProject.instance().layerTreeRoot()

# mapThemesCollection = QgsProject.instance().mapThemeCollection()
# mapThemes = mapThemesCollection.mapThemes()
# # Where you need to set your images names
# # Could be retrieve if only raster names wanted with
# # [layer.name() for layer in QgsProject.instance().mapLayers().values() if isinstance(layer, QgsRasterLayer)]
# # If you want all layers names and filter them manually
# # [layer.name() for layer in QgsProject.instance().mapLayers().values()]
# layersToChanges = [
#     "CartoDB Light",
#     "OpenStreetMap",
#     "OpenTransports",
# ]  # Replace with your list of raster layers instead


# for layer in layersToChanges:
    for child in root.children():
        if isinstance(child, QgsLayerTreeGroup):
            print("- group: " + child.name())
        elif isinstance(child, QgsLayerTreeLayer):
            print("- layer: " + child.name() + "  ID: " + child.layerId())
            # Layer you want to tick
            if child.name() == layer:
                child.setItemVisibilityChecked(True)
                print("Check only once")
            elif child.name() in layersToChanges:
                child.setItemVisibilityChecked(False)
                print("Check the others you want to hide")
    mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
        QgsProject.instance().layerTreeRoot(),
        iface.layerTreeView().model()
        # For QGIS 3.18+, instead of above line, use iface.layerTreeView().layerTreeModel()
    )
    mapThemesCollection.insert(layer, mapThemeRecord)