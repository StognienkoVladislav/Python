import dis


def greet(name):
    return 'Hello, ' + name + '!'


print(greet('Guido'))
print(greet.__code__.co_code)
print(greet.__code__.co_consts)
print(greet.__code__.co_varnames)

print(dis.dis(greet))