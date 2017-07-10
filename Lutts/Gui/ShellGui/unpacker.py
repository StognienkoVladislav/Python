#распаковывает архивы, созданные packer.py

import sys
from Lutts.Gui.ShellGui.packer import marker        #использ общую строку разделитель
mlen = len(marker)                                  #имена файлов след за строкой - разделителем

def unpack(ifile, prefix='new-'):
    for line in open(ifile):                        #по всем строкам входного файла
        if line[:mlen] != marker:
            output.write(line)                      #записать действ строки

        else:
            name = prefix + line[mlen: -1]          #или создать новый входной файл
            print('creating:', name)
            output = open(name, 'w')

if __name__ == '__main__': unpack(sys.argv[1])