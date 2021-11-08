import os
import os.path

from qgis.PyQt import QtWidgets, uic
from qgis.gui import QgsFileWidget
from qgis.core import QgsSettings

from ..core.layout import AreappPrintLayout

import numpy as np

HOME = os.path.expanduser("~")

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "create_template.ui")
)


class CreateTemplateDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None, necessaryThemes=None):
        """Constructor."""
        super(CreateTemplateDialog, self).__init__(parent)
        self.necessaryThemes = necessaryThemes
        self.setupUi(self)

    def accept(self) -> None:
        self.printLayout = AreappPrintLayout(
            layoutName=self.templateNameLineEdit.text(),
            necessaryThemes=self.necessaryThemes,
            layoutMdim=np.array(
                [int(self.nbLinesLineEdit.text()), int(self.nb_columnsLineEdit.text())]
            ),
        )
        self.printLayout.createLayout()
        super().accept()
