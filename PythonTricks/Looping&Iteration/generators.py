
def repeate_three_times(value):
    yield value
    yield value
    yield value


for x in repeate_three_times('Hey Three'):
    print(x)


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


def bounded_repeater_2(value, max_repeats):
    for i in range(max_repeats):
        yield value


for x in bounded_repeater('Hi', 5):
    print(x)


