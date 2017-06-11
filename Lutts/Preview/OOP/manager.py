from OOP.person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')


if __name__ == '__main__':
    #tom = Manager(name = 'Tom Doe', age = 50, pay=50000, job='manager')
    tom = Manager('Tom Doe', 50, 50000)
    print(tom.lastName())
    print(tom)
