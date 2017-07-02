from tkinter import *

root = Tk()
lablefont = ('times', 20, 'bold')                   #семейство, размер, стиль
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')              #желтый текст на черном фоне
widget.config(font=lablefont)                       #использовать увеличеный шрифт
widget.config(height=3, width = 20)                 #начальный размер: строк, символов
widget.pack(expand=YES, fill=BOTH)
root.mainloop()