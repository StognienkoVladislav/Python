from tkinter import *

class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand = YES, fill = BOTH)
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()             #при двойном щелчке на списке
        label = self.listbox.get(index)                 #извлечь выбранный текст
        self.runCommand(label)                          #и вызвать дейстиве или get(ACTIVE)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief = SUNKEN)
        sbar.config(command = list.yview)               #связать sbar и list
        list.config(yscrollcommand = sbar.set)          #сдвиг 1 = сдвиг другого
        sbar.pack(side=RIGHT, fill=Y)                   #1 добавлен - посл обрезан
        list.pack(side=LEFT, expand = YES, fill=BOTH)   #список обрез 1
        pos = 0

        for label in options:                           #добавить в виджет списка
            list.insert(pos, label)                     #или insert(END, label)
            pos += 1                                    #или enumerate(options)

        list.config(selectmode = SINGLE, setgrid = 1)  #режимы выбора, измен. разм.
        list.bind('<Double-1>', self.handleList)        #установ обработку события
        self.listbox = list

    def runCommand(self, selection):
        print('You selected:', selection)

if __name__ == '__main__':
    options = (('Lumberjack - %s' % x) for x in range(20))  #или map/lambda
    ScrolledList(options).mainloop()