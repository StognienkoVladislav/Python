
import  _thread as thread, time

def counter(myId, count):       #эта функция выполняется в потоках
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId, i))

for i in range(5):                              #породить 5 потоков выполнения
    thread.start_new_thread(counter, (i, 5))    #каждый поток выполняет 5 циклов


time.sleep(6)
print('Main thread exiting.')
