import os, time

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                         #заставить родителя подождать
        msg = ('Spam %03d' % zzz).encode()      #каналы - двоичные файлы
        os.write(pipeout, msg)                  #отправить данные родителю
        zzz = (zzz + 1) % 5                     #переход к 0 после 4

def parent():
    pipein, pipeout = os.pipe()                 #создать канал с 2 концами
    if os.fork() == 0:                          #создать копию процесса
        child(pipeout)                          #в копии вызвать child

    else:                                       #в родителе слушать канал
        while True:
            line = os.read(pipein, 32)          #остановиться до получения данных
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

parent()