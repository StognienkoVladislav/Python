import os, sys
from Lutts.Tools.visitor import SearchVisitor

class EditVisitor(SearchVisitor):
    #открывает для редактирования файлы, содержащие искомую строку
    #и находящиеся в каталоге startDir и ниже

    editor = r'C:\cygwin\bin\vin-nox.exe'

    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))

if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))
