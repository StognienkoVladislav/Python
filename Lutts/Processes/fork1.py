#Ответвляет дочерние процессы, пока не будет нажата клавиша 'q'

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)     #Иначе будет возврат в родительский цикл

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()

        else:
            print('Hello from parent', os.getpid(), newpid)

        if input() == 'q':break

parent()