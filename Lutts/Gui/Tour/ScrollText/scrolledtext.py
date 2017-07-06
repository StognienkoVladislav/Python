#просто компонент просмотра текста или содержимого файла

print('ScrolledText')
from tkinter import *

class ScrolledText(Frame):
    def __init__(self, parent = None, text=' ', file = None):
        Frame.__init__(self, parent)
        self.pack(expand = YES, fill = BOTH)
        self.makeWidgets()
        self.settext(text, file)

    def makeWidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief = SUNKEN)
        sbar.config(command = text.yview)           #связать sbar и text
        text.config(yscrollcommand = sbar.set)
        sbar.pack(side=RIGHT, fill = Y)
        text.pack(side=LEFT, expand = YES, fill = BOTH)
        self.text = text

    def settext(self, text='', file = None):
        if file:
            text = open(file, 'r').read()

        self.text.delete('1.0', END)        #удалить текуший текст
        self.text.insert('1.0', text)       #добавить в стр. 1, кол.0
        self.text.mark_set(INSERT, '1.0')   #установить курсор вставки
        self.text.focus()                   #сэкономить щелчок мышью

    def gettext(self):                              #возвращает строку
        return self.text.get('1.0', END + '-1c')    #от начала до конца

if __name__ == '__main__':
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])     #имя файла в командной строке

    else:
        st = ScrolledText(text='Words\ngo here')    #иначе: две строки

    def show(event):
        print(repr(st.gettext()))

    root.bind('<Key-Escape>', show)
    root.mainloop()