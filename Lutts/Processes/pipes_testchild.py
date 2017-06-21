import os, time, sys
mypid = os.getpid()
parentid = os.getppid()

sys.stderr.write('Child %d of %d got arg: "%s"\n' %
                 (mypid, parentid, sys.argv[1]))

for i in range(2):
    time.sleep(3)           #приостановить родительский процесс
    recv = input()          #stdin связан с каналом: данные будут поступать из
                            #родительского потока вывода stdout
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, recv)
    print(send)             #stdout связан с каналом: данные будут поступать в
                            #родительский поток ввода stdin
    sys.stdout.flush()      #гарантировать отправку, иначе процесс заблокируется
