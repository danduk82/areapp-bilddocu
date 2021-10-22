import os
from PyQt5.QtWidgets import QGraphicsScale
from PyQt5.QtGui import QIcon

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.gui import QgsFileWidget
from qgis.core import QgsSettings
from qgis.utils import iface


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "config.ui"))


class ConfigDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.text = ""
        self.serverUrlLineEdit.setText(QgsSettings().value("/areapp/serverUrl", ""))

    def accept(self) -> None:

        self.text = self.serverUrlLineEdit.text
        super().accept()
        # validation OK button box
        # self.validationButtonBox.accepted.connect(self.save)
