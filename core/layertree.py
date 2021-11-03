from qgis.core import QgsCoordinateReferenceSystem, QgsProject, QgsRasterLayer


WMTS_CAPABILITIES_URL = "https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml"
CRS = "EPSG:2056"


WMTS_CAPABILITIES_URL = "https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml"
CRS = "EPSG:2056"
LV95 = QgsCoordinateReferenceSystem(2056, QgsCoordinateReferenceSystem.EpsgCrsId)


LAYERCONFIG = {
    "landeskarte": {
        "tilematrix": "2056_27",
        "layername": "ch.swisstopo.pixelkarte-farbe",
        "year": "current",
    },
    "swissimage": {
        "tilematrix": "2056_28",
        "layername": "ch.swisstopo.swissimage-product",
        "year": "current",
    },
}


class AreappLayertree:
    def __init__(self) -> None:
        self.layerList = [i for i in range(1974, 2021)]
        self.layerList.append("landeskarte")
        self.refresh()

    def refresh(self):
        for layer in self.layerList:
            self.addLayer(layer)

    def addLayer(self, layerToAdd):
        layerToAdd = str(layerToAdd)

        layername = (
            LAYERCONFIG["landeskarte"]["layername"]
            if layerToAdd == "landeskarte"
            else LAYERCONFIG["swissimage"]["layername"]
        )
        tilematrix = (
            LAYERCONFIG["landeskarte"]["tilematrix"]
            if layerToAdd == "landeskarte"
            else LAYERCONFIG["swissimage"]["tilematrix"]
        )
        year = (
            LAYERCONFIG["landeskarte"]["year"]
            if layerToAdd == "landeskarte"
            else layerToAdd
        )
        if len(QgsProject().instance().mapLayersByName(layerToAdd)) == 0:
            layer = QgsRasterLayer(
                f"contextualWMSLegend=0&crs=EPSG:2056&dpiMode=7&featureCount=10&format=image/jpeg&layers={layername}&styles={layername}&tileDimensions=Time%3D{year}&tileMatrixSet={tilematrix}&url=https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml",
                layerToAdd,
                "wms",
            )
            layer.setCrs(LV95)
            QgsProject.instance().addMapLayer(layer)
            node = QgsProject.instance().layerTreeRoot().findLayer(layer.id())
            if node:
                node.setItemVisibilityChecked(False)
