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
from PyQt5.uic.uiparser import QtCore

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.core import QgsPointXY, QgsSettings, QgsProject
from qgis.utils import iface
import re

import swagger_client

from ..core.bilddoku_item import BilddokuItem, DEFAULT_SCALE
from .. import resources

from .config_widget import ConfigDialog
from .create_template import CreateTemplateDialog

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
        self.bilddokuItem = None
        self.setupUi(self)
        self.parent = parent
        self.reset()
        self.setupLogic()

    def reset(self):
        # Initialize server config
        self.setServerConfig()
        self.bilddokuItem = BilddokuItem(self.serverConfig)
        self.coordinatesLineEdit.clear()
        self.UOWLineEdit.clear()
        self.swissNamesLineEdit.clear()
        self.swissNamesLineEdit.readOnly = True
        self.communeLineEdit.clear()
        self.communeLineEdit.readOnly = True
        self.refreshScale(DEFAULT_SCALE)
        self.mScaleWidget.setScale(DEFAULT_SCALE)
        self.remarkGeneralPlainTextBrowser.clear()
        self.refreshSelectLayoutComboBox()

    def setupLogic(self):

        # button "settings"
        self.configPushButton.clicked.connect(self.openConfigDlg)

        # initialize bilddokuItem
        self.nextPushButton.clicked.connect(self.next)

        # setup scalebar widget
        self.mScaleWidget.scaleChanged.connect(self.refreshScale)
        self.mScaleWidget.scaleChanged.connect(self.bilddokuItem.setScale)

        # setup coordinates input
        self.coordinatesLineEdit.returnPressed.connect(self.recenterMapCanvas)

        # setup cancel button
        self.cancelBilddokuPushButton.clicked.connect(self.reset)
        self.openCreateTemplateDlgPushButton.clicked.connect(self.openCreateTemplateDlg)

        # setup print layout logic
        QgsProject.instance().layoutManager().layoutAdded.connect(
            self.refreshSelectLayoutComboBox
        )
        QgsProject.instance().layoutManager().layoutRemoved.connect(
            self.refreshSelectLayoutComboBox
        )
        QgsProject.instance().layoutManager().layoutRenamed.connect(
            self.refreshSelectLayoutComboBox
        )

    def refreshSelectLayoutComboBox(self, text=None):
        self.selectTemplateComboBox.clear()
        self.printLayouts = QgsProject.instance().layoutManager().printLayouts()
        self.selectTemplateComboBox.addItems([l.name() for l in self.printLayouts])
        self.selectTemplateComboBox.setCurrentIndex(
            int(
                QgsSettings().value(
                    "/areapp/current_layout", self.selectTemplateComboBox.currentIndex()
                )
            )
        )
        # TODO: save the ID in the QgsSettings, and use it too.
        # Also add a test if too big (somebody could delete a layout)
        # Add a signal when a new layout is created so that the combobox gets an update

    def next(self):
        self.bilddokuItem.next()
        self.coordinatesLineEdit.setText(self.bilddokuItem.getCoordinatesStr())
        self.recenterMapCanvas()
        self.bilddokuItem.setScale(DEFAULT_SCALE)
        self.refreshScale(DEFAULT_SCALE)
        self.mScaleWidget.setScale(DEFAULT_SCALE)

        self.swissNamesLineEdit.setText(
            self.bilddokuItem.getSwissname()[0]
        )  # FIXME: ceci devrait être un menu déroulant
        self.swissNamesLineEdit.readOnly = True
        self.communeLineEdit.setText(self.bilddokuItem.getCommune())
        self.communeLineEdit.readOnly = True
        self.remarkGeneralPlainTextBrowser.setPlainText(
            self.bilddokuItem.getSpecificRemark()
        )
        scale = DEFAULT_SCALE
        self.refreshScale(scale)
        self.mScaleWidget.setScale(scale)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def refreshScale(self, scale: float):
        # iface.mapCanvas().zoomScale(scale)
        for canvas in iface.mapCanvases():
            canvas.zoomScale(scale)

    def openConfigDlg(self):
        dlg = ConfigDialog(iface.mainWindow())
        result = dlg.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.setServerConfig()

    def openCreateTemplateDlg(self):
        dlg = CreateTemplateDialog(iface.mainWindow())
        result = dlg.exec_()

    def setServerConfig(self):
        self.serverConfig = swagger_client.Configuration()
        host = QgsSettings().value(
            "/areapp/serverUrl",
            "https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.7",
        )
        self.serverConfig.host = host
        if self.bilddokuItem:
            self.bilddokuItem.setConfiguration(self.serverConfig)

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
