from PyQt5.QtWidgets import QApplication
import sys
from raipy.GUi import GUIWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=GUIWindow()
    sys.exit(app.exec_())