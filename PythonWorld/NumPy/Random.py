

#1 создавать списки, используя строенныйы модуль,
#  а затем преобразовывать их в numpy.array

import numpy as np
import random
print(np.array([random.random() for i in range(10)]))

#для создания массивов со случ элементами служит numpy.random

#все в промежутке [0, 1)
print(np.random.sample())
print(np.random.sample(3))
print(np.random.sample((2, 3)))

#С помощью randint или random_integers можно создать массив из целых чисел
print(np.random.randint(0, 3, 10))
print(np.random.random_integers(0, 3, 10))
print(np.random.randint(0, 3, (2, 10)))
#low/hight/size



#Можно юзать uniform для равномерного распределения

print(np.random.uniform(2, 8, (2, 10)))


####Выбор и перемешиывание
#Перемешать NumPy массив можно с помощью функции shuffle

a = np.arange(10)
print(a)

np.random.shuffle(a)
print(a)

#Можно заюзать permutation с 1 переменной, вернет перемешаный массив до N элемента
print(np.random.permutation(10))


#Сделать случайную выборку из массива можно с помощью функции choice
#Последний аргумент влияет на вероятность, по умолчанию = равномерное распределение
a = np.arange(10)
print(a)

print(np.random.choice(a, 10, p = [0.5, 0.25, 0.25, 0, 0, 0, 0, 0, 0, 0]))


###Инициализация генератора случайных чисел
#seed(число) - инициализация генератора

np.random.seed(1000)
np.random.random(10)

#get_state и set_state - возвращают и устанавливают состояние генератора
np.random.seed(1000)
state = np.random.get_state()
np.random.random(10)

np.random.set_state(state)
np.random.random(10)
