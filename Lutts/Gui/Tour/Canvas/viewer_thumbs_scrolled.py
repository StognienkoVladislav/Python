import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from Lutts.Gui.Tour.viewer_thumbs import makeThumbs, ViewOne

def viewer(imgdir, kind=Toplevel, numcols=None, height=300, width=300):

    win = kind()
    win.title('Simple viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(side=BOTTOM, fill=X)

    canvas = Canvas(win, borderwidth=0)
    vbar = Scrollbar(win)
    hbar = Scrollbar(win, orient='horizontal')

    vbar.pack(side=RIGHT, fill=Y) # прикрепить холст после полос прокрутки
    hbar.pack(side=BOTTOM, fill=X) # чтобы он обрезался первым
    canvas.pack(side=TOP, fill=BOTH, expand=YES)

    vbar.config(command=canvas.yview) # обработчики событий
    hbar.config(command=canvas.xview) # перемещения полос прокрутки
    canvas.config(yscrollcommand=vbar.set) # обработчики событий
    canvas.config(xscrollcommand=hbar.set) # прокрутки холста
    canvas.config(height=height, width=width) # начальные размеры видимой
# области, изменяемой при
# изменении размеров окна
    thumbs = makeThumbs(imgdir) # [(imgfile, imgobj)]
    numthumbs = len(thumbs)
    if not numcols:
        numcols = int(math.ceil(math.sqrt(numthumbs))) # фиксиров. или N x N
    numrows = int(math.ceil(numthumbs / numcols)) # истинное деление в 3.x

    linksize = max(thumbs[0][1].size) # (ширина, высота)
    fullsize = (0, 0, # верхний левый угол X,Y
        (linksize * numcols), (linksize * numrows) ) # нижний правый угол X,Y
    canvas.config(scrollregion=fullsize) # размер области


    rowpos = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:numcols], thumbs[numcols:]
        colpos = 0
        for (imgfile, imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(canvas, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=linksize, height=linksize)
            link.pack(side=LEFT, expand=YES)
            canvas.create_window(colpos, rowpos, anchor=NW,
                window=link, width=linksize, height=linksize)
            colpos += linksize
            savephotos.append(photo)
        rowpos += linksize
    return win, savephotos

if __name__ == '__main__':
    imgdir = '../gifs' if len(sys.argv) < 2 else sys.argv[1]
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()