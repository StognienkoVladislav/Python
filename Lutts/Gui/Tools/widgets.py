from tkinter import *

def frame(root, side=TOP, **extras):
    widget = Frame(root)
    widget.pack(side=side, expand = YES, fill=BOTH)
    if extras: widget.config(**extras)
    return widget

def label(root, side, text, **extras):
    widget = Label(root, text=text, relief=RIDGE)           #настройки по умолчанию
    widget.pack(side=side, expand = YES, fill=BOTH)         #авто компановка
    if extras: widget.config(**extras)                      #применить все
    return widget                                           #доп параметры

def button(root, side, text, command, **extras):
    widget = Button(root, text=text, command = command)
    widget.pack(side=side, expand = YES, fill=BOTH)
    if extras: widget.config(**extras)
    return widget

def entry(root, side, linkvar, **extras):
    widget = Entry(root, relief=SUNKEN, textvariable = linkvar)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras: widget.config(**extras)
    return widget

if __name__ == '__main__':
    app = Tk()
    frm = frame(app, TOP)           #требуется намного меньше кода
    label(frm, LEFT, 'SPAM')
    button(frm, BOTTOM, 'Press', lambda :print('Pushed'))
    mainloop()