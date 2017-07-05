gifdir = "gifs/"
from tkinter import *

win = Tk()
img = PhotoImage(file=gifdir + "1.gif")
Button(win, image = img).pack()
win.mainloop()