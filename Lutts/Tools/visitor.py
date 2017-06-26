import os, sys

class FileVisitor:
    #Выполн обход всех файлов, не являющихся каталогами
    #переключения трассировки trace: 0 - нет трассировки
    #1 - подкаталоги, 2 - добавляются файлы

    def __init__(self, context=None, trace=2):
        self.fcount = 0
        self.dcount = 0
        self.context = context
        self.trace = trace

    def run(self, startDir = os.curdir, reset = True):
        if reset: self.reset()
        for (thisDir, dirsHere, filesHere) in os.walk(startDir):
            self.visitdir(thisDir)
            for fname in filesHere:                             #для некаталогов
                fpath = os.path.join(thisDir, fname)            #fname не содержит пути
                self.visitfile(fpath)

    def reset(self):                                            #используется обходчиками,
        self.fcount = self.dcount = 0                           # выполняющими обход независимо

    def visitdir(self, dirpath):                                #вызывается для каждого каталога
        self.dcount += 1                                        #переопределить или расширить
        if self.trace > 0: print(dirpath, '...')

    def visitfile(self, filepath):                              #вызывается для каждого файла
        self.fcount += 1                                        #переопределить или расширить
        if self.trace > 1: print(self.fcount, '=>', filepath)


class SearchVisitor(FileVisitor):
    #Выполняется поиск в файлах, находящихся в каталоге startDir и ниже

    skipexts = []
    testexts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']     #допустимые расш.
   #skipexts = ['.gif', '.jpg', '.pyc', '.o', '.a', '.exe']     #или недопустимые расширения

    def __init__(self, searchkey, trace=2):
        FileVisitor.__init__(self, searchkey, trace)
        self.scount = 0

    def reset(self):                                            #в независимых обходчиках
        self.scount = 0

    def candidate(self, fname):                                 #переопределить, если желательно
        ext = os.path.splitext(fname)[1]                        #использовать модуль mimetypes
        if self.testexts:
            return ext in self.testexts                         #если допустимое расширение

        else:                                                   #или, если недопустимое
            return ext not in self.skipexts                     #расширение

    def visitfile(self, fname):                                 #поиск строки
        FileVisitor.visitfile(self, fname)
        if not self.candidate(self, fname):
            if self.trace > 0: print('Skipping', fname)

        else:
            text = open(fname).read()                           #'rb' для недекодируемого текста
            if self.context in text:                            #иди text.find() != -1
                self.visitmatch(fname, text)
                self.scount += 1

    def visitmatch(self, fname, text):                          #обработка совпадения
        print('%s has %s' % (fname, self.context))              #переопределить

if __name__ == '__main__':
    #логика самотестирования
    dolist = 1
    dosearch = 2                    #3 = список и поиск
    donext = 4                      #при добавлении следующего теста

    def selftest(testmask):
        if testmask & dolist:
            visitor = FileVisitor(trace=2)
            visitor.run(sys.argv[2])
            print('Visited %d files and %d dirs' %
                  (visitor.fcount, visitor.dcount))

        if testmask & dosearch:
            visitor = SearchVisitor(sys.argv[3], trace = 0)
            visitor.run(sys.argv[2])
            print('Found in %d files, visited %d' %
                  (visitor.scount, visitor.fcount))

selftest(int(sys.argv[1]))          #например, 3 = dolist | dosearch


