#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget
#Значок приложения
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()


    def initUi(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




