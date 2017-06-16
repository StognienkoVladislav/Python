import sys

def filter_files(name, function):       #фильтрация файлов через функцию
    input = open(name, 'r')             #создать обьекты файлов
    output = open(name + '.out', 'w')   #выходной файл
    for line in input:
        output.write(function(line))    #записать измен строку
    input.close()
    output.close()                      #выходной файл имеет расширение '.out'

def filter_stream(function):            #отсутствуют явные файлы
    while True:                         #использовать стандартные потоки
        line = sys.stdin.readline()     #или input()
        if not line: break
        print(function(line), end='')   #или sys.stdout.write()

if __name__ == '__main__':
    filter_stream(lambda line: line)    #копировать stdin в stdout, если
                                        #запущен как самостоятельный сценарий