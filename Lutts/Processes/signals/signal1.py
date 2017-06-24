import sys, signal, time
def now(): return time.ctime(time.time())           #строка с текущим временем

def onSignal(signum, stackframe):                   #обработчик сигнала
    print('Got signal', signum, 'at', now())        #большинство обработчиков
                                                    # остаются действующими
signum = int(sys.argv[1])
signal.signal(signum, onSignal)                     #установить обработчик сигнала
while True: pass                                    #ждать сигнал или :pass
