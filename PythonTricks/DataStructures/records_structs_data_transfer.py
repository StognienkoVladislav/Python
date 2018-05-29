import dis
from typing import NamedTuple
from struct import Struct

# dict - simple data object

car1 = {
    'color': 'red',
    'mileage': 4132.42,
    'automatic': True
}

car2 = {
    'color': 'blue',
    'mileage': 54123,
    'automatic': False
}

print(car2)
print(car2['mileage'])

# Dicts are mutable:
car2['mileage'] = 12
car2['windshield'] = 'broken'
print(car2)

# Tuple - immutable groups of objects
print(dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval')))


# NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car_tuple = Car('red', 42.9, True)
print(car_tuple)

# Fields are immutable
# car_tuple.mileage = 12

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.3)
print(data)
print(MyStruct.unpack(data))
