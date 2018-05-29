

class Dog:
    num_legs = 4    # <- Class variable

    def __init__(self, name):
        self.name = name    # <- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')
print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)
print(Dog.num_legs)
# print(Dog.name)

Dog.num_legs = 6
print(jack.num_legs, jill.num_legs)


Dog.num_legs = 4
jack.num_legs = 6
print(jack.num_legs, jill.num_legs, Dog.num_legs)
print(jack.num_legs, jack.__class__.num_legs)


class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
