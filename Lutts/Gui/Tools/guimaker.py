import sys
from tkinter import *                           #классы виджетов
from tkinter.messagebox import showinfo

class GuiMaker(Frame):
    menuBar = []                        #значение по умолчанию
    toolBar = []                        #изменять при создании подклассов
    helpButton = True                   #устанавливать в start()

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)        #растягиваемый фрейм
        self.start()
        self.makeMenuBar()
        self.makeToolBar()
        self.makeWidgets()

    def makeMenuBar(self):
        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)

        for (name, key, items) in self.menuBar:
            mbutton = Menubutton(menubar, text=name, underline = key)
            mbutton.pack(side = LEFT)
            pulldown = Menu(mbutton)
            self.addMenuItems(pulldown, items)
            mbutton.config(menu = pulldown)

        if self.helpButton:
            Button(menubar, text = 'Help',
                            cursor = 'gumby',
                            relief = FLAT,
                            command = self.help).pack(side = RIGHT)

    def addMenuItems(self, menu, items):
        for item in items:                              #скан список вложенных элементов
            if item == 'separator':                     #строка: добавить разделитель
                menu.add_separator({})

            elif type(item) == list:                    #список неактивных элементов
                for num in item:
                    menu.entryconfig(num, state=DISABLED)

            elif type(item[2]) != list:
                menu.add_command(label    = item[0],    #команда метка
                                 underline = item[1],   #горячая клавиша
                                 command   = item[2])   #обр-к: вызов обьект

            else:
                pullover = Menu(menu)
                self.addMenuItems(pullover, item[2])    #подменю
                menu.add_cascade(label     = item[0],   #создать подменю
                                 underline = item[1],   #добавить каскад
                                 menu      = pullover)

    def makeToolBar(self):
        if self.toolBar:
            toolbar = Frame(self, cursor = 'hand2', relief = SUNKEN, bd=2)
            toolbar.pack(side=BOTTOM, fill=X)
            for (name, action, where) in self.toolBar:
                Button(toolbar, text=name, command = action).pack(where)

    def makeWidgets(self):
        name = Label(self,
                     width = 40, height = 10,
                     relief = SUNKEN, bg='white',
                     text = self.__class__.__name__,
                     cursor = 'crosshair')
        name.pack(expand = YES, fill=BOTH, side=TOP)

    def help(self):
        showinfo('Help', 'Sorry, no help for ' + self.__class__.__name__)

    def start(self):
        pass

GuiMakerFrameMenu = GuiMaker            #использ для меню встраив компонентов

class GuiMakerWindowMenu(GuiMaker):
    def makeMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu = menubar)

        for (name, key, items) in self.menuBar:
            pulldown = Menu(menubar)
            self.addMenuItems(pulldown, items)
            menubar.add_cascade(label = name, underline = key, menu = pulldown)

        if self.helpButton:
            if sys.platform[:3] == 'win':
                menubar.add_command(label = 'Help', command = self.help)

            else:
                pulldown = Menu(menubar)        #в Linux требуется настоящее меню
                pulldown.add_command(labe = 'About', command = self.help)
                menubar.add_cascade(label = 'Help', menu=pulldown)

#самотестирование
if __name__ == '__main__':
    from Lutts.Gui.Tools.guimixin import GuiMixin   #встроить метод Help

    menuBar = [
        ('File', 0,
         [('Open', 0, lambda :0),
          ('Quit', 0, sys.exit)]),
        ('Edit', 0,
         [('Cut', 0, lambda :0),
          ('Paste', 0 , lambda :0)])]

    toolBar = [('Quit', sys.exit, {'side': LEFT})]

    class TestAppFrameMenu(GuiMixin, GuiMakerFrameMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

    class TestAppWindowMenu(GuiMixin, GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

    class TestAppWindowMenuBasic(GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar                      #help из GuiMaker, а не из GuiMixin

    root = Tk()
    TestAppFrameMenu(Toplevel())
    TestAppWindowMenu(Toplevel())
    TestAppWindowMenuBasic(root)
    root.mainloop()