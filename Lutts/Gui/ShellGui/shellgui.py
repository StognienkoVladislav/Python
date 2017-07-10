from tkinter import *
from Lutts.Gui.Tools.guimaker import *
from Lutts.Gui.Tools.guimixin import GuiMixin

class ShellGui(GuiMixin, GuiMakerWindowMenu):

    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title("Shell Tools Listbox")
        self.master.iconname("Shell Tools")


    def handleList(self, event):                        #двойной щелчок на список
        label = self.listbox.get(ACTIVE)                #получить выбранный текст
        self.runCommand(label)                          #выполнить операцию


    def makeWidgets(self):                              #добавить список в середину
        sbar = Scrollbar(self)                          #связать sbar со списком
        list = Listbox(self, bg='white')                #или использ Tour.ScrolledList
        sbar.config(command = list.yview)
        list.config(yscrollcommand = sbar.set)
        sbar.pack(side=RIGHT, fill=Y)                   #первым добавлен = посл. обрезан
        list.pack(side=LEFT, expand = YES, fill=BOTH)   #список обрез первым

        for (label, action) in self.fetchCommands():    #добав в список
            list.insert(END, label)                     #в меню и на панель инст

        list.bind('<Double-1>', self.handleList)        #установ обработчик
        self.listbox = list


    def forToolBar(self, label):
        return True                                     #по умолч поместить все на панель инст


    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label, action, dict(side=LEFT)))

        self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
            ('File', 0, [('Quit', -1, self.quit)]),     #имя раскрыв меню
            ('Tools', 0, toolEntries)                   #список элементов меню(метка/клавиша/обработчик)
        ]

        for (label, action) in self.fetchCommands():
            toolEntries.append((label, -1,action))      #добавить приложения в меню

#делегирование операций шаблон подклассам, которые в свою очередь
#делегируют операции подклассам, реализ запуск утилит

class ListMenuGui(ShellGui):
    def fetchCommands(self):                            #myMenu устанав в подклассе
        return self.myMenu                              #список кортежей(метка, обработчик)

    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd: action()

class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()

    def runCommand(self, cmd):
        self.myMenu[cmd]()
