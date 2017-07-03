from tkinter import *

def showPostEvent(event):
    print('Widget = %s X = %s Y = %s' % (event.widget, event.x, event.y))

def showAllEvent(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))

def onKeyPress(event):
    print('Got key press:', event.char)

def onArrowKey(event):
    print('Got up arrow key press')

def onReturnKey(event):
    print('Got return key press')

def onLeftClick(event):
    print('Got left mouse button click:', end=' ')
    showPostEvent(event)

def onRightClick(event):
    print('Got right mouse button click:', end=' ')
    showPostEvent(event)

def onMiddleClick(event):
    print('Got middle mouse button click:', end=' ')
    showPostEvent(event)
    showAllEvent(event)

def onLeftDtag(event):
    print('Got left button drag:', end=' ')
    showPostEvent(event)

def onDoubleLeftClick(event):
    print('Got double left mouse click', end=' ')
    showPostEvent(event)
    tkroot.quit()

tkroot = Tk()
labelfont = ('courier', 20, 'bold')
windget = Label(tkroot, text='Hello bind world')
