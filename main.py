from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication

from coffee_main import MainUi

if __name__ == "__main__":
    app = QApplication([])
    w = MainUi()
    app.exec_()
