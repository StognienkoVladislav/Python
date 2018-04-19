
"""

    __int__(self)
    Преобразование типа в int.

    __long__(self)
    Преобразование типа в long.

    __float__(self)
    Преобразование типа в float.

    __complex__(self)
    Преобразование типа в комплексное число.

    __oct__(self)
    Преобразование типа в восьмеричное число.

    __hex__(self)
    Преобразование типа в шестнадцатиричное число.

    __index__(self)
    Преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step]).
    Если вы определяете свой числовый тип, который может использоваться как индекс списка,
    вы должны определить __index__.

    __trunc__(self)
    Вызывается при math.trunc(self). Должен вернуть своё значение, обрезанное до целочисленного типа (обычно long).

    __coerce__(self, other)
    Метод для реализации арифметики с операндами разных типов. __coerce__ должен вернуть
    None если преобразование типов невозможно. Если преобразование возможно, он должен вернуть пару
    (кортеж из 2-х элементов) из self и other, преобразованные к одному типу.

"""