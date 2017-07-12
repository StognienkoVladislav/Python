try:
    import _thread as thread

except ImportError:
    import _dummy_thread as thread

#общая очередь

import sys, queue
threadQueue = queue.Queue(maxsize=0)

def threadChecker(widget, delayMsecs = 100, perEvent = 1):      #10раз/сек, 1 таймер

    for i in range(perEvent):
        try:
            (callback, args) = threadQueue.get(block=False)

        except queue.Empty:
            break

        else:
            callback(*args)                 #вызвать обработчик

    widget.after(delayMsecs,                                                #переустановить таймер и
                 lambda : threadChecker(widget, delayMsecs, perEvent))      #вернуться в цикл событий



def threaded(action, args, context, onExit, onFail, onProgress):
    try:
        if not onProgress:          #Ждать заверш этого потока
            action(*args)

        else:
            def progress(*any):
                threadQueue.put((onProgress, any + context))
            action(progress = progress, *args)

    except:
        threadQueue.put((onFail, (sys.exc_info(),) + context))

    else:
        threadQueue.put((onExit, context))

def startThread(action, args, context, onExit, onFail, onProgress = None):
    thread.start_new_thread(
        threaded, (action, args, context, onExit, onFail, onProgress)
    )

class ThreadCounter:
    def __init__(self):
        self.cont = 0
        self.mutex = thread.allocate_lock()         #или Threading.semaphore

    def incr(self):
        self.mutex.acquire()
        self.count += 1
        self.mutex.release()

    def decr(self):
        self.mutex.acquire()
        self.cont -= 1
        self.mutex.release()

    def __len__(self):return self.count

if __name__ == '__main__':
    import time
    from tkinter.scrolledtext import ScrolledText

    def onEvent(i):
        myname = 'thread-%s' % i
        startThread(
            action=threadaction,
            args = (i,3),
            context = (myname,),
            onExit = threadexit,
            onFail = threadfail,
            onProgress=threadprogress
        )

    #основная операция, выполн потоком
    def threadaction(id, reps, progress):       #то, что делает поток
        for i in range(reps):
            time.sleep(1)
            if progress: progress(i)            #обработчик progress: в очередь
        if id % 2 == 1: raise Exception         #ошибочный номер: неудача

    #обработчики завершения/информирования о ходе выполнения задания:
    #передаются главному потоку через очередь
    def threadexit(myname):
        text.insert('end', '%s\texit\n' % myname)
        text.see('end')

    def threadfail(exc_info, myname):
        text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
        text.see('end')

    def threadprogress(count, myname):
        text.insert('end', '%s\tprog\t%s\n' % (myname, count))
        text.see('end')
        text.update()

    text = ScrolledText()
    text.pack()
    threadChecker(text)                         #Запустить цикл обработки потоков
    text.bind('<Button-1>',
              lambda event: list(map(onEvent, range(6))))   #для получения всех результатов map
    text.mainloop() #вход в цикл событий