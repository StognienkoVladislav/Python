import math


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
# print(MyClass.method())


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    # @classmethod
    # def margherita(cls):
    #     return cls(['mozzarella', 'tomatoes'])

    # @classmethod
    # def prosciutto(cls):
    #    return cls(['mozzarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
# Pizza(['cheese', 'tomatoes'])
# print(Pizza.margherita())


p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza.circle_area(4))
