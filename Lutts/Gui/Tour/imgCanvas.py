gifdir = "gifs/"
from tkinter import *

win = Tk()
img = PhotoImage(file = gifdir + "Circles-3.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(1, 1, image = img, anchor = NW)
win.mainloop()