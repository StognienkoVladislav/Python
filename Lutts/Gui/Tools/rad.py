#динамически перегружает обработчики

from tkinter import *
from imp import reload
from Lutts.Gui.Tools import radactions          #получить первонач обработчики


class Hello(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        Button(self, text='message1', command = self.message1).pack(side = LEFT)
        Button(self, text='message2', command = self.message2).pack(side = RIGHT)

    def message1(self):
        reload(radactions)                      #перезагрузить модуль перед вызовом
        radactions.message1()                   #теперь зелчок на кнопке вызовет новую версию

    def message2(self):
        reload(radactions)
        radactions.message2(self)

    def method1(self):
        print('exposed method...')              #вызыв из функц в модуле radactions

Hello().mainloop()