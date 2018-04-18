import sys

from PyQt5.QtWidgets import QApplication
from CrosPlat.Application import ApplicationWindow
from Application import ApplicationWindow

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()
