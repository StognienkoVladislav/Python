import datetime


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')


my_car = Car('red', 123431)
print(my_car)
print(str([my_car]))
print(my_car.color, my_car.mileage)


# repr/str for date
today = datetime.date.today()
print(str(today))
print(repr(today))
