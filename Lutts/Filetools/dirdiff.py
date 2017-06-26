#Порядок использования: python dirdiff.py dir1-path dir2-path

import os, sys

def reportdiffs(unique1, unique2, dir1, dir2):
    #генерирует отчет о различиях для одного каталога: часть вывода функции comparedirs

    if not (unique1 or unique2):
        print('Directory lists are identical')

    else:
        if unique1:
            print('Files unique to', dir1)
            for file in unique1:
                print('...', file)

        if unique2:
            print('Files unique to', dir2)
            for file in unique2:
                print('...', file)

def difference(seq1, seq2):
    #Возвращает элементы, присутствующие только в seq1 (set(seq1) - set(seq2))

    return [item for item in seq1 if item not in seq2]

def comparedirs (dir1, dir2, files1 = None, files2 = None):
    #сравнивает содержимое каталогов, но не сравнивает содержимое файлов

    print('Comparing', dir1, 'to', dir2)
    files1 = os.listdir(dir1) if files1 is None else files1
    files2 = os.listdir(dir2) if files2 is None else files2

    unique1 = difference(files1, files2)
    unique2 = difference(files2, files1)

    reportdiffs(unique1, unique2, dir1, dir2)
    return not (unique1 or unique2)                 #true, если нет различий

def getargs():
    #Аргументы при работе в режиме командной строки
    try:
        dir1, dir2 = sys.argv[1:]                   #2 аргумента командной строки

    except:
        print('Usage: dirdiff.py dir1 dir2')
        sys.exit(1)

    else:
        return(dir1, dir2)

if __name__ == '__main__':
    dir1, dir2 = getargs()
    comparedirs(dir1, dir2)