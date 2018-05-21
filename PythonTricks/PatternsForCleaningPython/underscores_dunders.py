
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


t = Test()
print(t.foo, t._bar)


# def make_object(name, class):
    # SyntaxError

def make_object(name, class_):
    pass

class MangledMethod:

    def __method(self):
        return 42

    def call_it(self):
        return self.__method()

# MangledMethod().__method()
# AttributeError
MangledMethod().call_it()
# 42

_MangledGlobal__mangled = 23


class MangledGlobal:
    def test(self):
        return __mangled


print(MangledGlobal().test())


class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42


print(PrefixPostfixTest().__bam__)

for _ in range(4):
    print("Test")

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color, mileage)


