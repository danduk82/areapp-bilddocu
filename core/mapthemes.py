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
        # create a maping between period:year
        self.DefineThemesFromPointAttributes(imagesAttributes)
        # check if the layer is present in layertree, otherwise load it
        self.AddLayersIfNeeded()
        # create the themes
        self.CreateThemes()
        # adapt the GUI, add canvases
        self.AddMapCanvasesIfNeeded()

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

    def AddLayersIfNeeded(self):
        pass

    def AddMapCanvasesIfNeeded(self):
        # TODO: sync with main view!!!!
        mapCanvasesThemes = []
        iface.mapCanvas().setTheme("main")
        for mapCanvas in iface.mapCanvases():
            mapCanvasesThemes.append(mapCanvas.theme())
        print(f"mapCanvasesThemes = {mapCanvasesThemes}")
        mapCanvasesThemes.remove("main")
        try:
            mapCanvasesThemes.remove("")
        except ValueError:
            pass

        allThemes = list(self.necessaryThemes.keys())
        print(f"allThemes = {allThemes}")
        allThemes.remove("main")
        try:
            allThemes.remove("")
        except ValueError:
            pass
        toDo = list(set(mapCanvasesThemes).symmetric_difference(set(allThemes)))
        print(f"toDo = {toDo}")

        for theme in toDo:
            mp = iface.createNewMapCanvas(theme)
            if mp:
                mp.setTheme(theme)

        # todo, add the correct setLayers
        # https://qgis.org/pyqgis/3.2/gui/Map/QgsMapCanvas.html#qgis.gui.QgsMapCanvas.setLayers

        # for theme, year in self.necessaryThemes.items():
        #     if theme == "main":
        #         allThemes.remove(theme)
        #         continue
        #     for mapCanvas in iface.mapCanvases():
        #         if mapCanvas.theme() in allThemes:
        #             try:
        #                 allThemes.remove(theme)
        #             except ValueError:
        #                 pass
        #             pass
        #         elif mapCanvas.theme() == "":
        #             mapCanvas.setTheme(theme)
        #         else:
        #             mp = iface.createNewMapCanvas(theme)
        #             if mp:
        #                 mp.setTheme(theme)

    def CreateThemes(self):
        mapThemesCollection = QgsProject.instance().mapThemeCollection()
        # FIXME: for the moment we reset all, but we could be smarter and have a
        #        method for this, which gets called by the gui if needed.
        for map_theme_name in sorted(self.necessaryThemes.keys()):
            if not mapThemesCollection.hasMapTheme(map_theme_name):
                new_map_theme = mapThemesCollection.createThemeFromCurrentState(
                    QgsProject.instance().layerTreeRoot(), iface.layerTreeView().model()
                )
                mapThemesCollection.insert(map_theme_name, new_map_theme)