import os, time

def counter(count):                             #вызывается в новом процессе
    for i in range(count):
        time.sleep(1)                           #имитировать работу
        print('[%s]=> %s' % (os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid !=0:                                 #в родительском процессе:
        print('Process %d spawned' %pid)        #продолжить цикл

    else:
        counter(5)                              #в дочернем процессе
        os._exit(0)                             #вызвать функцию и завершить

print('Main process exiting.')                  #родитель не должен ждать