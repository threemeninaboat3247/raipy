from PyQt5.QtWidgets import QApplication
from raipy.GUI import GUIWindow
import sys

def exe():
    app = QApplication(sys.argv)
    ex=GUIWindow()
    sys.exit(app.exec_())