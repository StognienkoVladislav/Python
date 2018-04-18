from PyQt5.QtWidgets import QFileDialog
import sklearn.linear_model as lm
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score


def basic_consider(df):
    lr = lm.LinearRegression()
    x = df.Hours_Studied[:, np.newaxis]
    y = df.Test_Grade
    lr.fit(x, y)
    pred = lr.predict(x)

    return x, y, pred


def consider_for_polynomial_degrees(_dynamic_ax, df):
    lr = lm.LinearRegression()
    x = df.Hours_Studied
    y = df.Test_Grade

    for deg in [1, 2, 3, 4, 5]:
        lr.fit(np.vander(x, deg + 1), y)
        y_lr = lr.predict(np.vander(x, deg + 1))
        _dynamic_ax.plot(x, y_lr, label='degree ' + str(deg))
        _dynamic_ax.legend(loc=2)
        print(r2_score(y, y_lr))


def showDialog(self):
    fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

    if fname[0]:
        df = pd.read_csv(fname[0])
        return df