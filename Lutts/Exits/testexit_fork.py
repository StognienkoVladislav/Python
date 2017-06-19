#Под Cygwin

import os
exitstat = 0

def child():           #здесь можно вызвать os.exit для завершения
    global exitstat     #изменит глобальную переменную этого процесса
    exitstat += 1       #код завершения для функции wait родителя
    print('Hello from child', os.getpid(), exitstat)
    os._exit(exitstat)
    print('never reached')


def parent():
    while True:
        newpid = os.fork()  #запустить новую копию процесса
        if newpid == 0:     #если это копия, вызвать функцию child
            child()         #ждать ввода 'q' с консоли

        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break

if __name__ == '__main__': parent()