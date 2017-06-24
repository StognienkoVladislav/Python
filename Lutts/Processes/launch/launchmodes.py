import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable         #использовать sys в последних версиях Python

def fixWindowsPath(cmdline):
    #замещает все / на \ в путях к сценариям

    splitline = cmdline.lstrip().split(' ')         #разбить по пробелам
    fixedpath = os.path.normpath(splitline[0])      #заменить прямые слешы
    return ' '.join([fixedpath] + splitline[1:])    #снова обьединить в строку

class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command

    def __call__(self):             #вызывается при вызове экземпляра,
        self.announce(self.what)    #например как обработчик щелчка на кнопке
        self.run(self.where)        #подклассы должны определять метод run()

    def announce(self, text):       #подклассы могут переопределять метод
        print(text)                 #announce() вместо логики if/elif

    def run(self, cmdline):
        assert False, 'run must be defined'

class System(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' %(pypath, cmdline))

class Popen(LaunchMode):
    #запускает команду оболочки в новом процессе

    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline)        #предпологается, что нет данных для чтения

class Fork(LaunchMode):

    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()                       #превращает строку в список
        if os.fork() == 0:                              #запустить новый процесс
            os.execvp(pypath, [pyfile] + cmdline)       #запустить новую программу

class Start(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)

class StartArgs(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start' + cmdline)                   #может создать окно консоли

class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))

class Top_level(LaunchMode):
    def run(self, cmdline):
        assert False, 'Sorry - mode not yet implemented'

#выбор "лучшего" средства запуска для данной платформы

if sys.platform[:3] == 'win':
    PortableLauncher = Spawn

else:
    PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass

def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()                                      #не блокирует

    input('system mode...')
    System(file, file)()                            #блокирует

    if sys.platform[:3] == 'win':
        input('DOS start mode...')                  #не блокирует
        StartArgs(file, file)()

if __name__ == '__main__' : selftest()