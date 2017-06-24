#взаимодействие через анонимные каналы

import os
from multiprocessing import Process, Pipe

def sender(pipe):
    #передает обьект родителю через анонимный канал
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()


def talker(pipe):
    #передает и принимает обьекты из канала
    pipe.send(dict(name='Bob', spam=42))
    reply = pipe.recv()
    print('talker got:', reply)

if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,)).start()    #породить потомка с каналом
    print('parent got:', parentEnd.recv())              #принять от потомка
    parentEnd.close()                                   #или закрыть автоматическим сборщиком мусора

    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()
    print('parent got:', parentEnd.recv())              #принять от потомка
    parentEnd.send({x * 2 for x in 'spam'})             #передать потомку
    child.join()                                        #ждать завершения потомка
    print('parent exit')
