from tkinter import *
from Lutts.Gui.Tour.alarms import alarm

class Alarm(alarm.Alarm):
    def repeater(self):
        self.bell()
        if self.master.state() == 'normal':             #окно отображается?
            self.master.withdraw()                      #скрыть окно, без ярлыка

        else:
            self.master.deiconify()                     #iconify свертывает в ярлык иначе перерисовать окно
            self.master.lift()                          #и поднять над остальными

        self.after(self.msecs, self.repeater)           #переустановить обработчик

if __name__ == '__main__': Alarm().mainloop()           #master = корневое окно Tk по умолчанию