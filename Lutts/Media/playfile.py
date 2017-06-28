import os, sys, mimetypes, webbrowser

helpmsg = """
Sorry: can`t find a media player for '%s' on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""

def trace(*args): print(*args)                      #с разделяющими пробелами

class MediaTool:
    def __init__(self, runtext = ''):
        self.runtext = runtext

    def run(self, mediafile, **options):            #options обычно игнорируется
        fullpath = os.path.abspath(mediafile)       #cwd может быть любым
        self.open(fullpath, **options)


class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')        #запустить команду оболочки
        player.write(media.read())                  #отправить файл в stdin


class Cmdline(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile          #запустить команду
        os.system(cmdline)                          #использовать %s для имени файла

class Winstart(MediaTool):                              #использует реестр Windows
    def open(self, mediafile, wait = False, **other):   #позволяет дождаться
        if not wait:                                    #окончания проигрывания файла
            os.startfile(mediafile)                     #или os.system('start file')

        else:
            os.system('start /WAIT ' + mediafile)

class Webbrowser(MediaTool):
    # file:// требует указывать абсолютный путь
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)

#соответствия платформ и проигрывателей

audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'), # os.popen().write()
    'linux2': Cmdline('cat %s > /dev/audio'), # по крайней мере в PDA Zaurus
    'sunos4': Filter('/usr/demo/SOUND/play'), # да, даже такая древность!
    'win32': Winstart()                       # startfile или system
                                              #'win32': Cmdline('start %s')
}
videotools = {
    'linux2': Cmdline('tkcVideo_c700 %s'), # PDA Zaurus
    'win32': Winstart(), # предотвратить вывод окна DOS
}
imagetools = {
    'linux2': Cmdline('zimager %s'), # PDA Zaurus
    'win32': Winstart(),
}
texttools = {
    'linux2': Cmdline('vi %s'), # PDA Zaurus
    'win32': Cmdline('notepad %s') # или попробовать PyEdit?
}
apptools = {
    'win32': Winstart() # doc, xls, и др.: используйте
                        # на свой страх и риск!
}


#таблица соответствия между типами файлов и программами - проигрывателями

mimetable = {
    'audio':        audiotools,
    'video':        videotools,
    'image':        imagetools,
    'text':         texttools,
    'application':  apptools
}

def trywebbrowser(filename, helpmsg = helpmsg, **options):
    """
    открывает в веб, если тип файла или платформы неизвестен
    """

    trace('trying browser', filename)
    try:
        player = Webbrowser()                   #открыть в браузере
        player.run(filename, **options)

    except:
        print(helpmsg % filename)               #никакой из способов не работает

def playknownfile(filename, playertable = {}, **options):
    #проигрывает медиафайл известного типа: использует программы-проигрыватели
    #для данной платформы или запускает веб-браузер

    if sys.platform in playertable:                         #известный
        playertable[sys.platform].run(filename, **options) #инструмент

    else:                                                   #универсальный
        trywebbrowser(filename, **options)                  #прием

def playfile(filename, mimetable = mimetable, **options):
    #проигрывает медиафайл любого типа

    contenttype, encoding = mimetypes.guess_type(filename)  #проверить имя
    if contenttype == None or encoding is not None:         #не определяется
        contenttype = '?/?'

    maintype, subtype = contenttype.split('/', 1)           #image/jpeg

    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)                  #спец случай

    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)     #по таблице

    else:
        trywebbrowser(filename, **options)                  #другие типы


if __name__ == '__main__':
    #тип медиафайла известен
    playknownfile('test.au', audiotools, wait=True)
    playknownfile('ora-pp3e.gif', imagetools, wait=True)
    playknownfile('ora-lp3e.jpg', imagetools)

    #тип медиафайла определяется
    input('Stop players and press Enter')
    playfile('ora-lp4e.jpg')                                #image/jpeg
    playfile('ora-pp3.gif')                                 #image/gif
    playfile('priorcalendar.html')                          #text/html
    playfile('lp4e-preface-previw.html')                    #text/html
    playfile('spam.doc')                                    #app
    playfile('spreadsheet.xls')                             #app
    playfile('sousa.au', wait=True)
    input('Done')                                           #приостановиться, если
                                                            # сценарий запущен щелчком мыши