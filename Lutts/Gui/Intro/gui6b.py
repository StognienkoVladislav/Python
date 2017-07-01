from sys import exit
from tkinter import *
from Lutts.Gui.Intro.gui6 import Hello

parent = Frame(None)            #контейнерный виджет
parent.pack()
Hello(parent).pack(side=RIGHT)  #прикрепить виджет Hello, не запуская его

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()