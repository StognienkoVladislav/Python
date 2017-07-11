import os, glob
from tkinter import Tk, Toplevel, Frame, YES, BOTH, RIDGE
from tkinter.messagebox import showinfo, askyesno

class _window:
    #подмешиваемый класс, используется классами главный и всплывающих окон

    foundicon = None            #совместно использ всеми экземп(может быть сброшен)
    iconpatt = '*.ico'
    iconmine = 'pu.ico'

    def configBorders(self, app, kind, iconfile):
       if not iconfile:
           iconfile = self.findIcon()

       title = app
       if kind: title += ' - ' + kind
       self.title(title)
       self.iconname(app)           #при свертывании
       if iconfile:
           try:
               self.iconbitmap(iconfile)

           except:
               pass

       self.protocol('WM_DELETE_WINDOW', self.quit)     #не закрывать без предупреждения

    def findIcon(self):
        if _window.foundicon:           #ярлык уже найден?
            return _window.foundicon

        iconfile = None
        iconshere = glob.glob(self.iconpatt)
        if iconshere:
            iconfile = iconshere[0]

        else:
            mymod = __import__(__name__)
            path = __name__.split('.')
            for mod in path[1:]:
                mymod = getattr(mymod, mod)

            mydir = os.path.dirname(mymod.__file__)
            myicon = os.path.join(mydir, self.iconmine)     #использ myicon, а не tk
            if os.path.exists(myicon): iconfile = myicon

        _window.foundicon = iconfile                        #не выполн поиск вторично
        return iconfile

class MainWindow(Tk, _window):
    #главное окно верхнего уровня

    def __init__(self, app, king='', iconfile = None):
        Tk.__init__(self)
        self.__app = app
        self.configBorders(app, king, iconfile)

    def quit(self):
        if self.okayToQuit():                               #запущены ли потоки
            if askyesno(self.__app, 'Verify Quit Program?'):
                self.destroy()                              #завершить приложение

            else:
                showinfo(self.__app, 'Quit not allowed')    #или в okayToQuit

    def destroy(self):
        Tk.quit(self)

    def okayToQuit(self):
        return True

class PopupWindow(Toplevel, _window):
    #вторичное всплывающее окно

    def __init__(self, app, kind='', iconfile = None):
        Toplevel.__init__(self)
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if askyesno(self.__app, 'Verify Quit Window?'):
            self.destroy()

    def destroy(self):
        Toplevel.destroy(self)

class QuietPopupWindow(PopupWindow):
    def quit(self):
        self.destroy()                      #закрывать без предупреждения

class ComponentWindow(Frame):
    #при присоединении к другим интерфейсам

    def __init__(self, parent):             #если не фрейм
        Frame.__init__(self, parent)        #предоставить контейнер
        self.pack(expand = YES, fill=BOTH)
        self.config(relief = RIDGE, border = 2) #перенастроить при необходимости

    def quit(self):
        showinfo('Quit', 'Not supported in attachment mode')

