#####################################################
#Классы
class Person:
    pass #Пустой блок
p = Person()
print(p)

#####################################################

#Методы обьектов
class Person:
    def sayHi(self):
        print('Darova')
p = Person()
p.sayHi()

#####################################################

#Метод __init__
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет! Меня зовут', self.name)
p = Person('Swaroop')
p.sayHi()

#####################################################

#Переменные класса и обьекта
class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Robot.population += 1

    def __del__(self):
        '''Удаление'''
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def sayHi(self):
        '''Приветствие'''
        print('Здарова! Меня зовут {0}.'.format(self.name))

    @staticmethod
    def howMany():
        print('У нас {0:d} роботов.'.format(Robot.population))

    #howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут выполнять работу.\n")

print("Конец работы")
del droid1
del droid2

Robot.howMany()

#####################################################

#Наследование

class SchoolMember:
    '''Представляет любогу человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    def tell(self):
        #Вывод инфы
        print('Имя:"{0} Возраст:"{1}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    #Класс преподавателя
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    #Представляет студента
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки Student: {0}'.format(self.marks))

t = Teacher('Mrs. Shriv',49,8000)
s = Student('Swaroop', 25,76)

print()

members = [t, s]
for member in members:
    member.tell()

#####################################################

#Метаклассы
from abc import *

class SchoolMember(metaclass=ABCMeta):
    '''Любой человек'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывод информации'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 8000)
s = Student('Swaroop', 25, 75)
print()

members = [t, s]
for member in members:
    member.tell() #работает для всех

#####################################################

#Ввод от пользователя
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")

#####################################################

#Файлы

poem = '''\
    Программировать весело.
    Если работа скучна,
    Чтобы придать ей веселый тон-
        используй Python!\n'''

f = open('poem.txt', 'w') #открываем записи
f.write(poem)
f.close()

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()

#####################################################

#Pickle
import pickle

#имя файла, в котором мы сохраним обьект
shoplistfile = 'shoplist data'

#список покупок
shoplist = ['яблоки', 'манго', 'морковь']

#Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) #помещаем обьект в файл
f.close()

del shoplist

#Счиьываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) #загружаем обьект из файла
print(storedlist)

#####################################################

#Обработка исключений
try:
    text = input('Введите что-нибудь -->')
except EOFError:
    print('Ну зачем вы сделали мне OEF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))

#####################################################

#Вызов исключения
class ShortInputException(Exception):
    '''Пользовательский класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    #проиходит работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки -- {0}; \
        ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений.')

#####################################################

#Try..Finally
import  time

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=" ")
        time.sleep(2)
except KeyboardInterrupt:
    print('!!Вы отменили чтение файла.!!')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')

#####################################################

#Оператор with
with open("poem.txt") as f:
    for line in f:
        print(line, end=' ')

#####################################################

#Модуль sys
import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы необходима как минимум\
                   верся Python 3.0",RuntimeWarning)
else:
    print('Нормальное продолжение')

#####################################################

#Модуль logging
import  os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),\
                                os.getenv('HOMEPATH'),\
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'test.log')

print("Сохраняем лог в", logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")

#####################################################

#Lambda-формы
points = [{'x' : 2, 'y' : 3},{'x' : 4, 'y' : 1}]
points.sort(key = lambda i:i['y'])
print(points)

#####################################################

#Генераторы списков
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i>2]
print(listtwo)

#####################################################

#Передача кортежей
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total
powersum(2, 3, 4) #25
powersum(2, 10) #100

#####################################################

