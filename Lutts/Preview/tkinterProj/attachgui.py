from tkinter import *
from tkinterProj.tkinter1 import MyGui

#Главное окно приложения
mainwin = Tk()
Label(mainwin, text=__name__).pack()

#окно диалога
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
