# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AreappDockWidget
                                 A QGIS plugin
 Areapp print layout
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-09-14
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Camptocamp SA
        email                : info@camptocamp.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import os.path
from PyQt5.QtWidgets import QDialog, QGraphicsScale
from PyQt5.QtGui import QIcon
from PyQt5.uic.uiparser import QtCore

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.gui import QgsFileWidget
from qgis.core import QgsPointXY, QgsSettings
from qgis.utils import iface
import re

from .. import swagger_client

from ..core.layout import AreappPrintLayout
from ..core.bilddoku_item import BilddokuItem
from .. import resources

from .config_widget import ConfigDialog

HOME = os.path.expanduser("~")

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "areapp_dockwidget_base.ui"),
    from_imports=True,
    resource_suffix="",
    import_from="areapp",
)


class AreappDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(AreappDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.parent = parent

        # validation OK button box
        # self.validationButtonBox.accepted.connect(self.print)

        self.configPushButton.clicked.connect(self.openConfig)

        # # setup file selection widget
        # self.outputPdfFileWidget.setFilter("*.pdf")
        # self.outputPdfFileWidget.setStorageMode(QgsFileWidget.SaveFile)
        # self.outputPdfFileWidget.setConfirmOverwrite(True)

        # Initialize server config
        self.setServerConfig()

        self.bilddokuItem = BilddokuItem()

        # setup scalebar widget
        self.mScaleWidget.scaleChanged.connect(self.refreshScale)

        # setup coordinates input
        self.coordinatesLineEdit.returnPressed.connect(self.recenterMapCanvas)

        self.printLayout = AreappPrintLayout()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def refreshScale(self, scale: float):
        # iface.mapCanvas().zoomScale(scale)
        for canvas in iface.mapCanvases():
            canvas.zoomScale(scale)

    def openConfig(self):
        dlg = ConfigDialog(iface.mainWindow())
        result = dlg.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.setServerConfig()

    def setServerConfig(self):
        self.serverConfig = swagger_client.Configuration()
        host = QgsSettings().value(
            "/areapp/serverUrl",
            "https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.4",
        )

    def print(self):
        # QgsSettings().value("/areapp/tmpFolder", "/tmp/pdf")
        # QgsSettings().value("/areapp/outputFolder", os.path.join(HOME, "areapp", "pdf"))
        # QgsSettings().value("/areapp/serverUrl", "")
        pass
        # filePath = self.outputPdfFileWidget.filePath()
        # scale = self.mScaleWidget.scale()
        # center = self.catch_coordinates(self.coordinatesLineEdit.text())
        # if filePath and center:
        #     self.printLayout.print(filePath, center, scale)

    def recenterMapCanvas(self):
        coordinates = self.catch_coordinates(self.coordinatesLineEdit.text())
        if isinstance(coordinates, QgsPointXY):
            iface.mapCanvas().setCenter(coordinates)

    @staticmethod
    def catch_coordinates(text):
        if text:
            lon_lat_match = re.match(r"^(\d+(\.?\d+?)?),(\d+(\.?\d+?)?)$", text)
            if lon_lat_match:
                lon = float(lon_lat_match[1])
                lat = float(lon_lat_match[3])
                selected = {"label": "{},{}".format(lon, lat), "lon": lon, "lat": lat}
                return QgsPointXY(lon, lat)
        return None
