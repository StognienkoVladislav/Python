
def null_decorator(func):
    return func


def greet():
    return 'Hello!'


greet = null_decorator(greet)
print(greet())


@null_decorator
def greet():
    return 'Hello!'


print(greet())


# Decorators Can Modify Behavior

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hello!'


print(greet())


# Applying Multiple Decorators to a Function
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@strong
@emphasis
def greet():
    return 'Hello!'


print(greet())


# Decorating Functions That Accept Arguments
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}()'
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}()'
              f'returned {original_result}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say('Jane', 'Hello, World'))
