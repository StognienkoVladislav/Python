#класс, "подмешиваемый" во фреймы: реализует общие методы
#вызова стандартных диалогов, запуск программ, простых инструментов
# отображения текста и т.д.

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from Lutts.Processes.launch.launchmodes import System, PortableLauncher
from Lutts.Gui.Tour.ScrollText.scrolledtext import ScrolledText


class GuiMixin:
    def infobox(self, title, text, *args):
        return showinfo(title, text)

    def errorbox(self, text):
        showerror('Error', text)

    def question(self, title, text, *args):
        return askyesno(title, text)                #вернет True или False

    def notdone(self):
        showerror('Not implemented', 'Option not available')

    def quit(self):
        ans = self.question('Verify qui', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)                        #нерекурсивный вызов quit!

    def help(self):                                 #переопределите более
        self.infobox('RTFM', 'See figure1...')      #подходящим

    def selectOpenFile(self, file="", dir="."):     #использ стандарт диалоги
        return askopenfilename(initialdir = dir, initialfile = file)

    def selectSaveFile(self, file="", dir="."):
        return asksaveasfilename(initialfile = file, initialdir = dir)

    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__                    #обьект класса экземпляра(самого низшего)
        myclass(new, *args)                         #прикрепить экземпляр к новому окну

    def spawn(self, pycmdline, wait = False):
        if not wait:                                    #запустить новй процесс
            PortableLauncher(pycmdline, pycmdline())    #запустить программу

        else:
            System(pycmdline, pycmdline)()

    def browser(self, filename):
        new = Toplevel()
        view = ScrolledText(new, file=filename)
        view.text.config(height = 30, width = 85)
        view.text.config(font=('courier', 10, 'normal'))    #моноширинный шрифт
        new.title("Text Viewer")
        new.iconname("browser")

if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):           #автономный тест
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command = self.quit).pack(fill=X)
            Button(self, text='help', command = self.help).pack(fill=X)
            Button(self, text='clone', command = self.clone).pack(fill=X)
            Button(self, text='spawn', command = self.other).pack(fill=X)

        def other(self):
            self.spawn('guimixin.py')           #запустить себя в отдельном процессе

    TestMixin().mainloop()