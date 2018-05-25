
add = lambda x, y: x + y
print(add(5, 3))


# equal
def add(x, y):
    return x + y


print(add(5, 3))
print((lambda x, y: x + y)(5, 3))


# Some kind of lambdas
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))
print(sorted(range(-5, 6), key=lambda x: x*x))


def make_adder(n):
    return lambda x: x+n


plus_5 = make_adder(5)
print(plus_5(4))


