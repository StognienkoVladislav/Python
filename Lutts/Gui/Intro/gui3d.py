import sys
from tkinter import *

class HelloCallable:
    def __init__(self):                 #__init__ вызывает при создании обьекта
        self.msg = 'Hello __call__ world'

    def __call__(self):
        print(self.msg)                 #__call__ вызвается при попытке обратиться
        sys.exit()                      #к обьекту класса как к функции

widget = Button(None, text='Hello event world', command = HelloCallable())
widget.pack()
widget.mainloop()

