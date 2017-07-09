import sys, os

from tkinter import *
from Lutts.Gui.Tools.guimaker import *
from Lutts.Gui.Tools.guimixin import *

class Hello(GuiMixin, GuiMakerWindowMenu):
    def start(self):
        self.hellos = 0
        self.master.title("GuiMaker Demo")
        self.master.iconname("GuiMaker")
        def spawnme(): self.spawn('big_gui.py')       #отлож вызов вместо lambda

        self.menuBar = [                            #дерево: 3 раскр меню
            ('File', 0,
                [('New...', 0, spawnme),
                 ('Open...', 0, self.fileOpen),     #[список элементов меню]
                 ('Quit', 0, self.quit)]),          #метка, клавиша, обработчик

            ('Edit', 0,
             [('Cut', -1, self.notdone),
              ('Paste', -1, self.notdone),
              'separator',                          #разделитель
              ('Stuff', -1,
               [('Clone', -1, self.clone),          #каскадное подменю
                ('More', -1, self.more)]
               ),
              ('Delete', -1, lambda :0),
              [5]]                                  #отключить 'delete'
             ),

            ('Play', 0,
             [('Hello', 0, self.greeting),
              ('Popup...', 0, self.dialog),
              ('Demos', 0,
               [('Toplevels', 0,
                 lambda : self.spawn(r'..\Tour\toplevel2.py')),
                ('Frames', 0,
                 lambda :self.spawn(r'..\Tour\demoAll-frm.py')),
                ('Images', 0,
                 lambda :self.spawn(r'..\Tour\buttonpics.py')),
                ('Alarm', 0,
                 lambda :self.spawn(r'..\Tour\alarms\alarm.py', wait=False)),
                ('Other...', -1, self.pickDemo)]
               )]
             )]

        self.toolBar = [                                                 #добавить 3 кнопки
            ('Quit', self.quit,dict(side=RIGHT)),
            ('Hello', self.greeting, dict(side=LEFT)),
            ('Popup', self.dialog, dict(side=LEFT, expand=YES))]

    def makeWidgets(self):
        middle = Label(self, text='Hello maker world!',
                       width = 40, height = 10,
                       relief = SUNKEN, cursor='pencil', bg='white')
        middle.pack(expand = YES, fill=BOTH)

    def greeting(self):
        self.hellos += 1
        if self.hellos % 3:
            print('Hi')

        else:
            self.infobox('Three', 'Hello!')             #каждый третий щелчок

    def dialog(self):
        button = self.question('OOPS!',
                               'You typed "rm*" ... continue?' ,        #старый стиль
                               'questhead', ('yes', 'no'))              #аргументы игнорируются
        [lambda : None, self.quit][button]()

    def fileOpen(self):
        pick = self.selectOpenFile(file='big_gui.py')

        if pick:
            self.browser(pick)

    def more(self):
        new = Toplevel()
        Label(new, text='A new non-modal window').pack()
        Button(new, text='Quit', command = self.quit).pack(side=LEFT)
        Button(new, text='More', command = self.more).pack(side=RIGHT)

    def pickDemo(self):
        pick = self.selectOpenFile(dir='..')
        if pick:
            self.spawn(pick)                        #запустить любую программу Python

if __name__ == '__main__': Hello().mainloop()
