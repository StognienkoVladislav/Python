#создает фрейм ряд с меткой и полем ввода и дополнительной кнопкой
#вызывающей диалог выбора файла

from tkinter import *                               #виджеты и константы
from tkinter.filedialog import askopenfilename      #диалог выбора файла

def makeFormRow(parent, label, width=15, browse = True, extend = False):
    var = StringVar()
    row = Frame(parent)
    lab = Label(row, text = label + '?', relief = RIDGE, width = width)
    ent = Entry(row, relief = SUNKEN, textvariable = var)
    row.pack(fill=X)                                #использ фреймы-ряды
    lab.pack(side=LEFT)                             #с метками фиксированной длины
    ent.pack(side=LEFT, expand = YES, fill=X)       #можно использ grid(row, col)

    if browse:
        btn = Button(row, text='browse...')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command =
                       lambda :var.set(askopenfilename() or var.get()))

        else:
            btn.config(command =
                       lambda : var.set(var.get() + ' ' + askopenfilename()))

    return var