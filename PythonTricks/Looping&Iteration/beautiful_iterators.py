
numbers = [1, 2, 3]

for n in numbers:
    print(n)


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater('Hello')

for item in repeater:
    print(item)


# A simpler iterator class
class Repeater2:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


repeater = Repeater2('Hello')
for item in repeater:
    print(item)


# Bounded repeater

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


repeater = BoundedRepeater('Hello', 4)
for item in repeater:
    print(item)

