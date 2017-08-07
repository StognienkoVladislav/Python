

"""
ndarray.ndim - число измерений (чаще их называют "оси") массива.


ndarray.shape - размеры массива, его форма. Это кортеж натуральных чисел,
показывающий длину массива по каждой оси. Для матрицы из n строк и m столбов, shape будет (n,m).
Число элементов кортежа shape равно ndim.


ndarray.size - количество элементов массива.
Очевидно, равно произведению всех элементов атрибута shape.


ndarray.dtype - объект, описывающий тип элементов массива.
Можно определить dtype, используя стандартные типы данных Python.
NumPy здесь предоставляет целый букет возможностей, как встроенных,
например: bool_, character, int8, int16, int32, int64, float8, float16, float32, float64, complex64, object_,
так и возможность определить собственные типы данных, в том числе и составные.


ndarray.itemsize - размер каждого элемента массива в байтах.


ndarray.data - буфер, содержащий фактические элементы массива.
Обычно не нужно использовать этот атрибут, так как обращаться
к элементам массива проще всего с помощью индексов.
"""


import numpy as np



if __name__ == '__main__':

    a = np.array([1, 2, 3])         #создает обьект типа ndarray
    print(a)
    print(type(a))


    b = np.array([[1.5, 2, 3], [4, 5, 6]])
    print(b)

    #можно переопределить тип в момент создания
    b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype = np.complex)
    print(b)



    #создание массива с исходными данными по умолчанию

    print(np.zeros((3, 5)))
    print(np.ones((2, 2, 2)))

    #Функция eye() создает единичную матрицу(двумерный массив)
    print(np.eye(5))

    #функция empty() создает массив без его заполнения. Исходное содержимое
    #случайно заполн относ "мусора" в памяти
    print(np.empty((3, 3)))
    print(np.empty((4, 4)))


    #arange() вместо списков возвращает массивы
    print(np.arange(10, 30, 5))
    print(np.arange(0, 1, 0.1))

    #для float используют не arange , а linspace(,,кол-во нужных элементов)
    print(np.linspace(0, 2, 9))


    #fromfunction(): применяет функцию ко всем комбинациям индексов
    def f1(i, j):
        return 3 * i + j

    print(np.fromfunction(f1, (3, 4)))

    #если массив слишком большой, NumPy автоматом скрывает центральную часть
    print(np.arange(0, 3000, 1))

    #если нужна печать всего массива использ numpy.set_printoptions
    np.set_printoptions(threshold = np.nan)
