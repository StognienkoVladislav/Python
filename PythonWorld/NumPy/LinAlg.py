

#numpy.linalg позволяет делать многие операции из линейной алгебры

###Возведение в сетпень
#linalg.matrix_power(M, n)

###Разложение
#linalg.cholesky(a) - Разложение Холецкого
#linalg.qr(a[, model]) - QR разложение
#linalg.svd(a[, full_matrices, computer_uv]) - сингулярное разложение

###Некоторые характеристики матриц
#linalg.eig(a) - собственные значения и собственные векторы
#linalg.norm(x[, ord, axis]) - норма вектора или оператора
#linalg.cond(x[, p]) - число обусловленности
#linalg.det(a) - определитель
#linalg.slogdet(a) - знак и логарифм определителя
#(для изображения переполнения, если сам определитель очень маленький)

###Системы уравнений
#linalg.solve(a, b) - решает систему линейных уравнений Ax = b
#linalg.tensorsolve(a, b[, axes]) - решает тензорную систему линейных уравнений Ax = b
#linalg.lstsq(a, b[, rcond]) - метод наименьших квадратов
#linalg.inv(a) - обратная матрица

import numpy as np

if __name__ == '__main__':
    a = np.arange(18).reshape((2, 3, 3))
    print(a)
    print(np.linalg.det(a))