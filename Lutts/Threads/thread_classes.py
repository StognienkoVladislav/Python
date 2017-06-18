import  threading

class Mythread(threading.Thread):           #Подклас класса Thread
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count                  #Информация для каждого потока
        self.mutex = mutex                  #совместно используемые обьекты
        threading.Thread.__init__(self)     #вместо глобальных переменных

    def run(self):                          #run реализует логику потока
        for i in range(self.count):         #синхронизировать доступ к stdout
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex = threading.Lock()              #то же, что и thread.allocate_lock()
threads = []

for i in range(10):
    thread = Mythread(i, 100, stdoutmutex)  #созадть/запустить 10 потоков
    thread.start()                          #вызвать метод run потока
    threads.append(thread)

for thread in threads:
    thread.join()                           #ждать завершения потока
print('Main thread exiting.')
