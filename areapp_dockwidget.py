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
from PyQt5.QtWidgets import QGraphicsScale

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.gui import QgsFileWidget
from qgis.core import QgsPointXY
from qgis.utils import iface
import re

from .layout import AreappPrintLayout


FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "areapp_dockwidget_base.ui")
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

        # validation OK button box
        self.validationButtonBox.accepted.connect(self.print)

        # setup file selection widget
        self.outputPdfFileWidget.setFilter(".pdf")
        self.outputPdfFileWidget.setStorageMode(QgsFileWidget.SaveFile)
        self.outputPdfFileWidget.setConfirmOverwrite(True)

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

    def print(self):
        filePath = self.outputPdfFileWidget.filePath()
        if filePath:
            self.printLayout.print(filePath)

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
