from tkinter import *
from Lutts.Gui.ShellGui.unpacker import unpack
from Lutts.Gui.ShellGui.formrows import makeFormRow     #создание полей формы

def unpackDialog():
    win = Toplevel()
    win.title('Enter Unpack Parameters')
    var = makeFormRow(win, label='Input file', width = 11)
    win.bind('<Key-Return>', lambda event: win.destroy())
    win.grab_set()
    win.focus_set()             #сделать себя модальным
    win.wait_window()           #ждать возврата из диалога
    return var.get()            #или закрытия его окна

def runUnpackDialog():
    input = unpackDialog()                  #получить вход параметры из диалога
    if input != '':
        print('Unpacker:', input)
        unpack(ifile = input, prefix='')

if __name__ == '__main__':
    Button(None, text='popup', command = runUnpackDialog).pack()
    mainloop()