import sys, signal, time
def now(): return time.asctime()

def onSignal(signum, stackframe):                   #обработчик сигнала
    print('Got alarm', signum, 'at', now())         #большинство обработчиков
                                                    #остаются действующими

while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, onSignal)         #установить обработчик сигнала
    signal.alarm(5)                                 #послать сигнал через 5 секунд
    signal.pause()                                  #ждать сигнала