import sys, os

def lister(root):                                              #для корневого каталога
    for (thisdir, subshere, fileshere) in os.walk(root):       #перечисляет
        print('[' + thisdir +']')                              #каталоги в дереве
        for fname in fileshere:                                #вывод файлов в каталоге
            path = os.path.join(thisdir, fname)                #добавить имя каталога
            print(path)

if __name__ == '__main__':                                     #имя каталога в
    lister(sys.argv[1])                                        #командной строке