
"""
    __cmp__:
    Все виды сравнениея, переопределить, когда все необходимые сравнения
    оперируют одним критерием
    """

"""
    __eq__(self, other)
    Определяет поведение оператора равенства, ==.
    
    __ne__(self, other)
    Определяет поведение оператора неравенства, !=.
    
    __lt__(self, other)
    Определяет поведение оператора меньше, <.
    
    __gt__(self, other)
    Определяет поведение оператора больше, >.
    
    __le__(self, other)
    Определяет поведение оператора меньше или равно, <=.
    
    __ge__(self, other)
    Определяет поведение оператора больше или равно, >=.
"""


class Word(str):
    """Класс для слов, определяющий сравнение по длине слов."""

    def __new__(cls, word):
        # Мы должны использовать __new__, т.к. тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]   #Теперь word это все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)
