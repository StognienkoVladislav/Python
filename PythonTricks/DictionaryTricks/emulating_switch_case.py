

def myfunc(a, b):
    return a + b


funcs = [myfunc]
print(funcs[0](2, 3))


def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


print(dispatch_if('mul', 2, 8))
print(dispatch_if('unknown', 2, 8))


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_dict('mul', 2, 8))
print(dispatch_dict('unknown', 2, 8))

