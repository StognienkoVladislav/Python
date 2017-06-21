#os.mkfifo

import os, time, sys
fifoname = '/tmp/pipefifo'      #имена должны быть одинаковывми

def child():
    pipeout = os.open(fifoname, os.O_WRONLY)    #открыть fifo как дескриптор
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %3d\n' % zzz).encode()     #был открыт в двоичном режиме
        os.write(pipeout, msg)
        zzz = (zzz+1) % 5

def parent():
    pipein = open(fifoname, 'r')                #открыть fifo как текстовый файл
    while True:
        line = pipein.readline()[:-1]           #блокируется до отправки данных
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))

if __name__ == '__main__':
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)                     #создать именованный канал

    if len(sys.argv) == 1:
        parent()          #есди нет аргументов - запустить как родительский процесс

    else:
        child()           #иначе - как дочерний процесс