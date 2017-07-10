#выводит диалог ввода параметров для сценария packer и запускает его

from glob import glob
from tkinter import *
from Lutts.Gui.ShellGui.packer import pack
from Lutts.Gui.ShellGui.formrows import makeFormRow

def packDialog():                       #новое окно верхнего уровня
    win = Toplevel()                    #с 2 фреймами-рядами + кнопка
    win.title('Enter Pack Parameters')
    var1 = makeFormRow(win, label='Output file')
    var2 = makeFormRow(win, label='Files to pack', extend = True)
    Button(win, text='Ok', command = win.destroy).pack()
    win.grab_set()
    win.focus_set()                     #модальный: захватить мушь, фокус ввода
    win.wait_window()                   #ждать закрытия окна диалога
                                        #иначе возврат произойдет немедленно
    return var1.get(), var2.get()       #извлечь значения связанных переменных

def runPackDialog():
    output, patterns = packDialog()     #вывести диалог и ждать щелчка на
    if output != '' and patterns != '': #кнопке Ok или закрытия окна
        patterns = patterns.split()     #выполнить действия не связ с граф интерф
        filenames = []
        for sublist in map(glob, patterns): #вып расшир шаблона вручную
            filenames += sublist            #командные оболочки Unix

        print('Packer:', output, filenames) #автомат
        pack(ofile=output, ifiles=filenames)        #Также можно вывести на граф интерф

if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command = runPackDialog).pack(fill=X)
    Button(root, text='bye', command = root.quit).pack(fill=X)
    root.mainloop()