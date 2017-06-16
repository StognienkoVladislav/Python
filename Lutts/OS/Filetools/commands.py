from sys import argv
from Filetools.scanfile import scanner
class UnknownCommand(Exception): pass

def processLine(line):  #определить функцию
    if line[0] == '*':  #применяему к каждой строке
        print("Ms.", line[1:-1])

    elif line[0] == '+':
        print("Mr.", line[1:-1])    #отбросить 1 и последни символ

    else:
        raise UnknownCommand(line)

filename = 'data.txt'
if len(argv)==2: filename = argv[1] #аргумент командной строки с именем
scanner(filename, processLine())    #файла запускает сканер