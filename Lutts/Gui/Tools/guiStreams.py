from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.scrolledtext import ScrolledText

class GuiOutput:
    font = ('courier', 9, 'normal')
    def __init__(self, parent=None):
        self.text = None
        if parent: self.popupnow(parent)        #сейчас или при первой записи

    def popupnow(self, parent=None):            #сейчас в родителе, Toplevel потом
        if self.text: return
        self.text = ScrolledText(parent or Toplevel())
        self.text.config(font=self.font)
        self.text.pack()

    def write(self, text):
        self.popupnow()
        self.text.insert(END, str(text))
        self.text.see(END)
        self.text.update()                      #обнов после каждой строки

    def writelines(self, lines):                #строки уже включают '\n'
        for line in lines: self.write(line)     #или map(self.write, lines)

class GuiInput:
    def __init__(self):
        self.buff = ''

    def inputLine(self):
        line = askstring('GuiInput', 'Enter input line + <crlf> (cancel = eof)')
        if line == None:
            return ''

        else:
            return line +'\n'

    def read(self, bytes = None):
        if not self.buff:
            self.buff = self.inputLine()

        if bytes:                               #читать по счетчику байтов
            text = self.buff[:bytes]            #чтобы не захватить лишние строки
            self.buff = self.buff[bytes:]

        else:
            text = ''                           #читать до eof
            line = self.buff
            while line:
                text = text + line
                line = self.inputLine()         #до cancel = eof = ''

        return text

    def readline(self):
        text = self.buff or self.inputLine()    #имитировать методы чтения файла
        self.buff = ''
        return text

    def readlines(self):
        lines = []                              #читать все строки
        while True:
            next = self.readline()
            if not next: break
            lines.append(next)
        return lines

def redirectedGuiFunc(func, *pargs, **kargs):
    import sys                                  #отображ потоки функции
    saveStreams = sys.stdin, sys.stdout         #во всплыв окна
    sys.stdin = GuiInput()                      #вывод диалог при необходимости
    sys.stdout = GuiOutput()                    #новое окно для каждого вызова
    sys.stderr = sys.stdout
    result = func(*pargs, **kargs)              #блокирующий вызов
    sys.stdin, sys.stdout = saveStreams
    return result

def redirectedGuiShellCmd(command):
    import os
    input = os.open(command, 'r')
    output = GuiOutput()
    def reader(input, output):
        while True:
            line = input.readline()
            if not line: break
            output.write(line)
    reader(input, output)

if __name__ == '__main__':
    def makeUpper():
        while True:
            try:
                line = input('Line? ')
            except:
                break
            print(line.upper())
        print('end of file')

    def makeLower(input, output):
        while True:
            line = input.readline()
            if not line: break
            output.write(line.lower())
        print('end of file')

    root = Tk()

    Button(root, text='test streams',
           command = lambda : redirectedGuiFunc(makeUpper)).pack(fill=X)

    Button(root, text='test files ',
           command = lambda : makeLower(GuiInput(), GuiOutput())).pack(fill=X)

    Button(root, text='test popen ',
           command = lambda : redirectedGuiShellCmd('dir *')).pack(fill=X)

    root.mainloop()