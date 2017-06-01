#Выражения
leng = 5
width = 2

area = leng * width
print(area)
print (2*(leng + width))

###################################################################

#Оператор if
number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print ('Вы угадали число')
elif guess < number:
    print ('Загаданное число больше этого')
else:
    print('Загаданное число меньше этого.')

print('Завершено')

###################################################################

#Оператор while
number = 23
running = True

while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Вы угадали')
        running = False
    elif guess < number:
        print('Загаданное число больше этого')
    else:
        print('Загаданное число меньше этого')
else:
    print('Цикл while закончен.')
print('Завершение.')

###################################################################

#Цикл for
for i in range(1,5):
    print(i)
else:
    print('Цикл for закончен')

###################################################################

#Оператор break
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки: ',len(s))
print('Завершение')

###################################################################

#Оператор continue
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введенная строка достаточной длины')

###################################################################

#Параметры функций
def printMax(a,b):
    if a > b:
        print(a, 'максимльно')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3,4)
x=5
y=7
printMax(x,y)

###################################################################

#Локальные переменные
x =50

def func(x):
    print('x равен', x)
    x = 2
    print('Замена локально x на ', x)
func(x)
print('x по прежнему', x)

###################################################################

#Зарезервированное слово"global"
x = 50
def func():
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func()
print('Значение x составляет', x)

###################################################################

#Зарезервированное слово "nonlocal"
def func_outer():
    x = 2
    print('x, равно',x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()

###################################################################

#Значения аргументов по умолчанию
def say(message, times = 1):
    print(message * times)
say('Привет')
say('Мир',5)

###################################################################

#Ключевые аргументы
def func(a, b=5, c=10):
    print('a равно', a,' b равно', b, ' с равно', c)
func(3,7)
func(25,c=24)
func(c=50,a=100)

###################################################################

#Переменное число параметров
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count +=number
    for key in keywords:
        count += keywords[key]
    return count
print(total(10,1,2,3,vegetables=50,fruits=100))

###################################################################

#Только ключевые параметры
def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print (count)
total(10,1,2,3,extra_number=50)
total(19,4,3,2) #Вызовет ошибку, поскольку мы не указали значение аргумента 'extra_number'

###################################################################

#Оператор "return"
def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y
print(maximum(2,5))

###################################################################

#Строки документации
def printMax(x,y):
    '''Выводит максимальное из двух чисел
       Оба значения дожны быть целыми числами '''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    elif x < y:
        print(y, 'наибольшее')
    else:
        print('равны')

printMax(3,5)
print(printMax.__doc__)

###################################################################

#Оператор from... import...(11.2)
from math import *
n = input('Введите диапазон:- ')
p = [2,3]
count = 2
a = 5
while(count < n):
    b = 0
    for i in range(2,a):
        if(i <= sqrt(a)):
            if(a%i == 0):
                print("a neptost",a)
                b = 1
            else:
                pass
    if (b != 1):
        print("a prost",a)
        p = p + [a]
    count = count + 1
    a = a +2
print (p)

###################################################################

#Cтруктуры данных
#Список покупок
shoplist = ['яблоки','манго','морковь','бананы']

print('Я должен сделать ', len(shoplist), 'покупок.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортируем свой список')
shoplist.sort()
print('Отсортированный список выглядит так:', shoplist)

print('Первоеб что мне нужно купить, это',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)

###################################################################

#Кортеж
zoo = ('питон', 'слон', 'пингвин')
print('Количество животных в зоопарке -',len(zoo))
new_zoo = 'обезьяна','верблюд',zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезенные из старого зоопарка:',new_zoo[2])
print('Последнее животное, привезенное из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1 + len(new_zoo[2]))

###################################################################

#Словарь
#'a'dress, 'b'ook

ab= {
    'Swaroop'   : 'swaroop@swaroopch.com',
    'Larry'     : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer'   : 'spammer@hotmail.com'
}

print("Адрес Swaroop`a:", ab['Swaroop'])

del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, adress in ab.items():
    print('Контакт {0} c адресом {1}'.format(name,adress))

#Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

###################################################################

#Последовательности
shoplistt = ['яблоки','манга', 'морковь', 'бананы']
name = 'swaroop'

#Операция индексирования
print('Элемент 0 -', shoplistt[0])
print('Элемент 1 -', shoplistt[1])
print('Элемент 2 -', shoplistt[2])
print('Элемент 3 -', shoplistt[3])
print('Элемент -1 -', shoplistt[-1])
print('Элемент -2 -', shoplistt[-2])
print('Символ 0 -', name[0])

#Вырезка из списка
print('Элементы с 1 по 3:', shoplistt[1:3])
print('Элементы с 2 до конца:', shoplistt[2:])
print('Элементы с 1 по -1:', shoplistt[1:-1])
print('Элементы от начала до конца:', shoplistt[:])

#Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1', name[1:-1])
print('Символы от начала до конца:', name[:])

###################################################################

#Ссылки
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist

del shoplist[0]

print('shoplist: ', shoplist)
print('mylist: ', mylist)
#Вывод один и тот же , т.к. mylist указывает на обьект shoplist

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]
del mylist[0]

print('shoplist:', shoplist)
print('mylist', mylist)
#Теперь списки разные

###################################################################

#Еще инфа по строкам
name = 'Swaroop'

if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')

if 'a' in name:
    print('Да, она содержит строку "a"')

if name.find('war')!= -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

###################################################################

