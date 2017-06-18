import threading, _thread
def action(i):
    print(i ** 32)

# подкласс, хранящий собственную информацию о состоянии
class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):                  #переопределить метод run
        print(self.i ** 32)

Mythread(2).start()                 #метод start вызовет метод run()

#передача простой функции
thread = threading.Thread(target=(lambda : action(2)))  #run вызовет target
thread.start()

#то же самое, но без lambda-функции,
#сохранящей информацию о состоянии в образуемом ей замыкании
threading.Thread(targer=action, args=(2,).start())      #вызываемый обьект
                                                        #и его аргументы

#с помощью модуля thread
_thread.start_new_thread(action, (2,))                  #полностью процедурный интерфейс

##############################################################################################

#обычный класс с атрибутами, ООП

class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i ** 32)

obj = Power(2)
threading.Thread(target=obj.action).start()             #запуск связанного метода

# вложенная область видимости, для сохранения информации о состоянии
def action(i):
    def power():
        print(i ** 32)
    return power

threading.Thread(target=action(2)).start()          #запуск возвращаемой функции

#запуск обоих вариантов с помощью модуля _thread
_thread.start_new_thread(obj.action, ())            #запуск вызываемого обьекта
_thread.start_new_thread(action(2), ())