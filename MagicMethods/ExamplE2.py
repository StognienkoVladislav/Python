
import time


class State:
    """Класс, хранящий строку и лог изменений. И забывающий свое значение после
    сериализации."""

    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        # Изменить значение. Зафиксировать последнее значение в истории.
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print('Changelog for Slate object:')
        for k, v in self.history.items():
            print('{}\t{}'.format(k, v))

    def __getstate__(self):
        # Намеренно не возращаем self.value or self.last_change.
        # Мы хотим чистую доску, после десериализации
        return self.history

    def __setstate__(self, state):
        self.history = state
        self.value, self.last_change = None, None
