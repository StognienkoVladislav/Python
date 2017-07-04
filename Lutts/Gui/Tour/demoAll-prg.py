from tkinter import *
from Lutts.Processes.launch.launchmodes import PortableLauncher

demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

for demo in demoModules:
    PortableLauncher(demo, demo + '.py')()          #запуск в виде программ верхнего уровня

root = Tk()
root.title('Processes')
Label(root, text='Multiple program demo: command lines', bg='white').pack()
root.mainloop()