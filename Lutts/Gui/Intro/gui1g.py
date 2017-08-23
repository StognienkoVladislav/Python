from tkinter import *
root = Tk()

widget = Label(root)
widget.config(text='Hello GUI_PyQt5 world!')
widget.pack(side=TOP, expand=YES, fill=BOTH)

root.title('gui1g.py')
root.mainloop()