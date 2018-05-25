

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(0, 1, 0)

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
print_vector(tuple_vec[0],
             tuple_vec[1],
             tuple_vec[2])


print_vector(*tuple_vec)
print_vector(*list_vec)


genexpr = (x*x for x in range(3))
print_vector(*genexpr)

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
print_vector(*dict_vec)


# Nothing to Return
"""
Python adds an implicit return None statement to the end of any
function. Therefore, if a function doesn’t specify a return value, it re-
turns None by default.
"""
def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    if value:
        return value


print(foo1(0))
print(type(foo2(0)))
