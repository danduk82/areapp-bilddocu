import os
import os.path

from qgis.PyQt import QtWidgets, uic
from qgis.gui import QgsFileWidget
from qgis.core import QgsSettings


HOME = os.path.expanduser("~")

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "config.ui"))


class ConfigDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)
        # temp folder
        self.tmpFolderQgsFileWidget.setStorageMode(QgsFileWidget.StorageMode(1))
        self.tmpFolderQgsFileWidget.setFilePath(
            QgsSettings().value("/areapp/tmpFolder", "/tmp/pdf")
        )
        # output folder
        self.outputFolderQgsFileWidget.setStorageMode(QgsFileWidget.StorageMode(1))
        self.outputFolderQgsFileWidget.setFilePath(
            QgsSettings().value(
                "/areapp/outputFolder", os.path.join(HOME, "areapp", "pdf")
            )
        )
        # server URL
        self.serverUrlLineEdit.setText(
            QgsSettings().value(
                "/areapp/serverUrl",
                "https://virtserver.swaggerhub.com/danduk82/bilddoku/1.0.5",
            )
        )

    def accept(self) -> None:
        # if validation OK button box is pressed, save the configuration
        # and ensure that the temp and output folders exist
        QgsSettings().setValue(
            "/areapp/tmpFolder", self.tmpFolderQgsFileWidget.filePath()
        )
        os.makedirs(self.tmpFolderQgsFileWidget.filePath(), exist_ok=True)
        QgsSettings().setValue(
            "/areapp/outputFolder", self.outputFolderQgsFileWidget.filePath()
        )
        os.makedirs(self.outputFolderQgsFileWidget.filePath(), exist_ok=True)
        QgsSettings().setValue("/areapp/serverUrl", self.serverUrlLineEdit.text())
        super().accept()
