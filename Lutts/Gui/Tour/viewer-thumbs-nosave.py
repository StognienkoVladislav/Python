#то же самое, но не сохраняет и не загружает миниатюры из файлов

import os, sys
from PIL import Image
from tkinter import Tk
from Lutts.Gui.Tour import viewer_thumbs


def makeThumbs(imgdir, size = (100, 100), subdir = 'thumbs'):
    #создает миниатюры в памяти, но не сохраняет их в файлах

    thumbs = []
    for imgfile in os.listdir(imgdir):
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = Image.open(imgpath)
            imgobj.thumbnail(size)
            thumbs.append(imgfile, imgobj)

        except:
            print("Skipping: ", imgpath)

    return thumbs

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'gifs'
    viewer_thumbs.makeThumbs = makeThumbs
    main, save = viewer_thumbs.viewer(imgdir, kind=Tk)
    main.mainloop()