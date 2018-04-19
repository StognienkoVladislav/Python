

class FunctionalList:
    """
    Класс-обертка над списком с добавлением некоторой функциональной магии:
    head, tail, init, last, drop, take.
    """

    def __init__(self, values = None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # если значение или тип ключа некорректны, list выбросит исключение
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # получить первый элемент
        return self.values[0]

    def tail(self):
        # получить все элементы после первого
        return self.values[1:]

    def init(self):
        # получить все элементы кроме последнего
        return self.values[:-1]

    def last(self):
        # получить последний элемент
        return self.values[-1]

    def drop(self, n):
        # все элементы кроме первых n
        return self.values[n:]

    def take(self, n):
        # первые n элементов
        return self.values[n:]
