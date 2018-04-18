
import numpy as np
import pandas as pd

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction, QFileDialog
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtWidgets import QLabel
from matplotlib.figure import Figure
from sklearn.metrics import r2_score
from views import basic_consider, consider_for_polynomial_degrees


class ApplicationWindow(QMainWindow):
    def __init__(self):

        df = pd.read_csv('Grade_Set_2.csv')

        super(ApplicationWindow, self).__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)

        openFile = QAction('&Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)

        x, y, pred = basic_consider(df)

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.scatter(x, y, color='black')
        self._static_ax.plot(x, pred, color='blue', linewidth=3)
        print("R squared", r2_score(y, pred))

        x = df.Hours_Studied
        y = df.Test_Grade
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        consider_for_polynomial_degrees(self._dynamic_ax, df)
        self._dynamic_ax.plot(x, y, 'ok')

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            df = pd.read_csv(fname[0])
            return df
