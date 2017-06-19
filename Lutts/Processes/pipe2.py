#обертывание входного дескриптора канала

import os, time

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                         #заставить родителя подождаь
        msg = ('Spam %03d\n' % zzz).encode()    #каналы - двоичные файлы в 3.Х
        os.write(pipeout, msg)                  #отправить данные родителю
        zzz = (zzz + 1) % 5                     #переход к 0 через 5 итераций


def parent():
    pipein, pipeout = os.pipe()                 #созадть канал с 2 концами
    if os.fork() == 0:                          #дочерний процесс пишет в канал
        os.close(pipein)                        #закрыть дескриптор ввода
        child(pipeout)

    else:                                       #в родителе слушать канал
        os.close(pipeout)                       #закрыть дескриптор вывода
        pipein = os.fdopen(pipein)              #создать обьект текстового файла
        while True:
            line = pipein.readline()[:-1]       #остановиться до получения данных
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


parent()