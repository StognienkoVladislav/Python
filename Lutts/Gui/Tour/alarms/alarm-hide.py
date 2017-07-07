#стирает и отображает кнопку в обработчике, устанавливаемом методов after()

from tkinter import *
from Lutts.Gui.Tour.alarms import alarm


class Alarm(alarm.Alarm):
    def __init__ (self, msecs = 1000):
        self.shown = False
        alarm.Alarm.__init__(self, msecs)

    def repeater(self):
        self.bell()                                 #подать сигнал
        if self.shown:
            self.stopper.pack_forget()              #скрыть кнопку

        else:
            self.stopper.pack()

        self.shown = not self.shown                 #изменить до след раза
        self.after(self.msecs, self.repeater)       #переустановить обработчик

if __name__ == '__main__': Alarm(msecs=500).mainloop()