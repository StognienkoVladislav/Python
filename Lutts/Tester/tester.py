import os, sys, glob, time
from subprocess import Popen, PIPE

#конфигурационные аргументы
testdir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
forcegen = len(sys.argv) > 2
print('Start tester:', time.asctime())
print('in', os.path.abspath(testdir))

def verbose(*args):
    print('-'*80)
    for arg in args: print(arg)
def quiet(*args): pass
trace = quiet

#отбор сценариев для тестирования
testpatt = os.path.join(testdir, 'Scripts', '*.py')
testfiles = glob.glob(testpatt)
testfiles.sort()
trace(os.getcwd(), *testfiles)

numfail = 0
for testpath in testfiles:                      #протестировать все сценарии
    testname = os.path.basename(testpath)       #отбросить путь к файлу

    #получить входной файл и аргументы для тестируемого сценария
    infile = testname.replace('.py', '.in')
    inpath = os.path.join(testdir, 'Inputs', infile)
    indata = open(inpath, 'rb').read() if os.path.exists(inpath) else b''

    argfile = testname.replace(',py', '.args')
    argpath = os.path.join(testdir, 'Args', argfile)
    argdata = open(argpath).read() if os.path.exists(argpath) else ''

    #местоположение файлов для сохранения stdout и stderr,
    #очистить предыдущие результаты

    outfile = testname.replace('.py', '.out')
    outpath = os.path.join(testdir, 'Outputs', outfile)
    outpathbad = outpath + '.bad'
    if os.path.exists(outpathbad): os.remove(outpathbad)

    errfile = testname.replace('.py', '.err')
    errpath = os.path.join(testdir, 'Errors', errfile)
    if os.path.exitsts(errpath): os.remove(errpath)

    #запустить тестируемый сценарий, перенаправив потоки ввода-вывода
    pypath = sys.executable
    command = '%s %s %s' % (pypath, testpath, argdata)
    trace(command, indata)

    process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.stdin.write(indata)
    process.stdin.close()

    outdata = process.stdout.read()
    errdata = process.stderr.read()     #при работе с двоичными файлами
    exitstatus = process.wait()         #данные имеют тип bytes
    trace(outdata, errdata, exitstatus)

    #проанализировать результат
    if exitstatus != 0:
        print('EROOR status:', testname, exitstatus)    #код завершения

    if errdata:                                         #и/или stderr
        print('ERROR stream:', testname, errpath)       #сохр. текст ошибки
        open(errpath, 'wb').write(errdata)

    if exitstatus or errdata:                           #оба признака ошибки
        numfail += 1                                    #можно получить код завершения + код ошибки
        open(outpathbad, 'wb').write(outdata)           #сохранить вывод

    elif not os.path.exists(outpath) or forcegen:
        print('generating:', outpath)                   #создать файл, если
        open(outpath, 'wb').write(outdata)              #необходимо

    else:
        priorout = open(outpath, 'rb').read()           #или сравнить с прежними
                                                        #результатами
        if priorout == outdata:
            print('passed:', testname)

        else:
            numfail += 1
            print('FAILED output:', testname, outpathbad)
            open(outpathbad, 'wb').write(outdata)

print('Finished:', time.asctime())
print('%s tests were run, %s tests failed.' % (len(testfiles), numfail))
