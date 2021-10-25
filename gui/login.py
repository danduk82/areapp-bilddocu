import os
import os.path

from qgis.PyQt import QtWidgets, uic
from qgis.gui import QgsFileWidget
from qgis.core import QgsSettings


HOME = os.path.expanduser("~")

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "login.ui"))


class LoginDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(LoginDialog, self).__init__(parent)
        self.username = None
        self.password = None
        self.usernameLineEdit.setText()
        self.passwordLineEdit.setText()

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
