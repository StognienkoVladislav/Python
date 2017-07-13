#Реализация полнофункционального текстового редактора
Version = '2.1'
import sys, os

from tkinter import *
from tkinter.filedialog import Open, SaveAs
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring, askinteger
from tkinter.colorchooser import askcolor
from Lutts.Gui.Tools.guimaker import *

#общие настройки
try:
    import textConfig
    configs = textConfig.__dict__
except:
    configs = {}


START = '1.0'                       #индекс 1 символа: строка = 1, столбец = 0
SEL_FIRST = SEL + '.first'          #отобразить тег sel в индекс
SEL_LAST  = SEL + '.last'           #то же, что 'sel.last'

FontScale = 0                       #использ увелич шрифт в Linux
if sys.platform[:3] != 'win':
    FontScale = 3

#Главные классы: реализуют граф интерфейс редактора, операции разновидности GuiMaker
#должны подмешиваться в более специализированные подклассы, а не наслед непосред,
#потому что этот класс принимает множество форм.

class TextEditor:           #смешать с классом Frame, имеющим меню/панель инструментов
    startfiledir = '.'      #для диалогов
    editwindows = []        #для проверки при завершении

    #Настройки порядка выбора кодировки
    #импортируются в класс, чтобы обеспечить возможность переопределения
    #в подклассе

    if __name__ == '__main__':
        from textConfig import(
        opensAskUser, opensEncoding,
        savesUseKnownEncoding, savesAskUser, savesEncoding
        )

    else:
        from .textConfig import(
        opensAskUser, opensEncoding,
        savesUseKnownEncoding, savesAskUser, savesEncoding
        )

    ftypes = [('All files', '*'),               #для диалога открытия файла
              ('Text files', '.txt'),           #настроить в подклассе или
              ('Python files', '.py')]          #устанавливать в каждом экземпляре

    colors = [
        {'fg' : 'black',        'bg' : 'white'},                #список цветов для выбора
        {'fg' : 'yellow',       'bg' : 'black'},                #первый элемент по умолчанию
        {'fg' : 'white',        'bg' : 'blue'},                 #элемент выбора PickBg/Fg
        {'fg' : 'black',        'bg' : 'beige'},
        {'fg' : 'yellow',       'bg' : 'purple'},
        {'fg' : 'black',        'bg' : 'brown'},
        {'fg' : 'lightgreen',   'bg' : 'darkgreen'},
        {'fg' : 'darkblue',     'bg' : 'orange'},
        {'fg' : 'orange',       'bg' : 'darkblue'}
    ]

    fonts = [
        ('courier',         9 + FontScale,  'normal'),          #шрифты, нейтральные
        ('courier',        12 + FontScale,  'normal'),          #в отношении платформы
        ('courier',        10 + FontScale,  'bold'),            #(семейство, размер, стиль)
        ('courier',        10 + FontScale,  'italic'),          #или вывести в списке
        ('times',          10 + FontScale,  'normal'),          #увеличить в Linux
        ('helvetica',      10 + FontScale,  'normal'),          #
        ('ariel',          10 + FontScale,  'normal'),
        ('system',         10 + FontScale,  'normal'),
        ('courier',        20 + FontScale,  'normal')
    ]

    def __init__(self, loadFirst = '', loadEncode = ''):

        if not isinstance(self, GuiMaker):
            raise TypeError('TextEditor needs a GuiMaker mixin')
        self.setFileName(None)
        self.lastfind   = None
        self.openDialog = None
        self.saveDialog = None
        self.knownEncoding = None
        self.text.focus()
        if loadFirst:
            self.update()
            self.onOpen(loadFirst, loadEncode)

    def start(self):
        self.menuBar = [
            ('File',0,
             [('Open...',       0,  self.onOpen),
              ('Save',          0,  self.onSave),
              ('Save As...',    5,  self.onSaveAs),
              ('New',           0,  self.onNew),
              'separator',
              ('Quit...',       0,  self.onQuit)]
            ),

            ('Edit',0,
             [('Undo',          0,  self.onUndo),
              ('Redo',          0,  self.onRedo),
              'separator',
              ('Cut',           0,  self.onCut),
              ('Copy',          1,  self.onCopy),
              ('Paste',         0,  self.onPaste),
              'separator',
              ('Delete',        0,  self.onDelete),
              ('Select All',    0,  self.onSelectAll)]
            ),

            ('Search',0,
             [('Goto...',       0,  self.onGoto),
              ('Find...',       0,  self.onFind),
              ('Refind',        0,  self.onRefind),
              ('Change...',     0,  self.onChange),
              ('Grep...',       3,  self.onGrep)]
             ),

            ('Tools',0,
             [('Pick Font...',  6,  self.onPickFont),
              ('Font List',     0,  self.onFontList),
              'separator',
              ('Pick Bg...',    3,  self.onPickBg),
              ('Pick Fg...',    0,  self.onPickFg),
              ('Color List',    0,  self.onColorList),
              'separator',
              ('Info...',       0,  self.onInfo),
              ('Clone',         1,  self.onClone),
              ('Run Code',      0,  self.onRunCode)]
             )]

        self.toolBar = [
            ('Save',    self.onSave,    {'side' : LEFT}),
            ('Cut',     self.onCut,     {'side' : LEFT}),
            ('Copy',    self.onCopy,    {'side' : LEFT}),
            ('Paste',   self.onPaste,   {'side' : LEFT}),
            ('Find',    self.onRefind,  {'side' : LEFT}),
            ('Help',    self.help,      {'side' : RIGHT}),
            ('Quit',    self.onQuit,    {'side' : RIGHT})
        ]

    def makeWidgets(self):                              #вызыв из GuiMaker.__init__
        name = Label(self, bg='black', fg='white')      #ниже меню, выше панели
        name.pack(side=TOP, fill=X)                     #компоновка меню/панелей
                                                        #фрейм GuiMaker компонуется сам

        vbar = Scrollbar(self)
        hbar = Scrollbar(self, orient = 'horizontal')
        text = Text(self, padx = 5, wrap = 'none')      #запретить перенос строк
        text.config(undo = 1, autoseparators = 1)

        vbar.pack(side = RIGHT,  fill=Y)
        hbar.pack(side = BOTTOM, fill=X)                #скомп текст последним(иначе обрежутся полосы прокрутки
        text.pack(side = TOP,    fill=BOTH, expand = YES)

        text.config(yscrollcommand = vbar.set)
        text.config(xscrollcommand = hbar.set)
        vbar.config(command = text.yview)
        hbar.config(command = text.xview)

        #применить пользовательские настройки
        startfont = configs.get('font', self.fonts[0])
        startbg   = configs.get('bg',   self.colors[0]['bg'])
        startfg   = configs.get('fg',   self.colors[0]['fg'])
        text.config(font = startfont, bg = startbg, fg = startfg)

        if 'height' in configs: text.config(height = configs['height'])
        if 'width'  in configs: text.config(width  = configs['width'])
        self.text = text
        self.filelabel = name

#Операции меню File

    def my_askopenfilename(self):           #обьекты запоминают каталог/файл
        if not self.openDialog:             #последней операции
            self.openDialog = Open(initialdir = self.startfiledir,
                                   filetypes  = self.ftypes)
        return self.openDialog.show()

    def my_asksaveasfilename(self):
        if not self.saveDialog:
            self.saveDialog = SaveAs(initialdir = self.startfiledir,
                                     filetypes  = self.ftypes)
        return self.saveDialog.show()

    def onOpen(self, loadFirst = '', loadEncode = ''):
        if self.text_edit_modified():
            if not askyesno('PyEdit',   'Text has changed: discard changes?'):
                return

        file = loadFirst or self.my_askopenfilename()
        if not file:
            return

        if not os.path.isfile(file):
            showerror('PyEdit', 'Could not open file ' + file)
            return

        #применить известную кодировку, если указана
        text = None             #пустой файл = " " = False
        if loadEncode:
            try:
                text = open(file, 'r', encoding=loadEncode).read()
                self.knownEncoding = loadEncode

            except(UnicodeError, LookupError, IOError):         #Lookup: ошибка в имени
                pass

        #прмиенить кодировку, введенную пользователем,
        #предварительно записать в диалог след вариант(по умолчанию)

        if text == None and self.opensAskUser:
            self.update()
            askuser = askstring('PyEdit', 'Enter Unicode encoding for open',
                                initialvalue = (self.opensEncoding or
                                                sys.getdefaultencoding() or ''))

            if askuser:
                try:
                    text = open(file, 'r', encoding = askuser).read()
                    self.knownEncoding = askuser
                except(UnicodeError, LookupError, IOError):
                    pass

        #применить кодировку из файла с настройками
        if text == None and self.opensEncoding:
            try:
                text = open(file, 'r', encoding = self.opensEncoding).read()
                self.knownEncoding = self.opensEncoding

            except(UnicodeError, LookupError, IOError):
                pass

        #применить системную кодировку по умолчанию(utf-8)
        if text == None:
            try:
                text = open(file, 'r',
                            encoding=sys.getdefaultencoding()).read()
                self.knownEncoding = sys.getdefaultencoding()
            except(UnicodeError, LookupError, IOError):
                pass

        #крайний случай: использ возможности Tk
        if text == None:
            try:
                text = open(file, 'rb').read()      #строка байтов
                text = text.replace(b'\r\n', b'\n') #для отображения
                self.knownEncoding = None

            except IOError:
                pass

        if text == None:
            showerror('PyEdit', 'Could not decode and open file ' + file)

        else:
            self.setAllText(text)
            self.setFileName(file)
            self.text.edit_reset()          #очистка стеков undo/redo
            self.text.edit_modified()       #сбросить флаг наличия изменений

    def onSave(self):
        self.onSaveAs(self.currfile)

    def onSaveAs(self, forcefile = None):
        filename = forcefile or self.my_asksaveasfilename()
        if not filename:
            return
        text = self.getAllText()
        encpick = None

        if self.knownEncoding and (
                (
                    forcefile and self.savesUseKnownEncoding >= 1
                )
            or (
                    not forcefile and self.savesUseKnownEncoding >=2
                )
        ):
            try:
                text.encode(self.knownEncoding)
                encpick = self.knownEncoding
            except UnicodeError:
                pass

        if not encpick and self.savesAskUser:
            self.update()
            askuser = askstring('PyEdit', 'Enter Unicode encoding for save',
                                initialvalue = (self.knownEncoding or
                                                self.savesEncoding or
                                                sys.getdefaultencoding() or ''))
        if askuser:
            try:
                text.encode(askuser)
                encpick = askuser
            except(UnicodeError, LookupError):
                pass

        if not encpick and  self.savesEncoding:
            try:
                text.encode(self.savesEncoding)
                encpick = self.savesEncoding

            except(UnicodeError, LookupError):
                pass

        if not encpick:
            try:
                text.encode(sys.getdefaultencoding())
                encpick = sys.getdefaultencoding()
            except(UnicodeError, LookupError):
                pass

        if not encpick:
            showerror('PyEdit', 'Could not encode for file ' + filename)

        else:
            try:
                file = open(filename, 'w', encoding = encpick)
                file.write(text)
                file.close()
            except:
                showerror('PyEdit', 'Could not write file ' + filename)

            else:
                self.setFileName(filename)
                self.text.edit_modified(0)
                self.knownEncoding = encpick

#////////////////////////////////////////////////////////////////////////////////////////////////////