
def yell(text):
    return text.upper() + '!'


print(yell('Hello'))


# Functions Are Objects
bark = yell
print(bark('woof'))

del yell
# print(yell('Some text'))
# Error

print(bark('hey'))
print(bark.__name__)


# Functions to DataStructures

funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f, f('hey there'))

print(funcs[0]('heyho'))


# Functions in functions
def greet(func):
    greeting = func('Hi, I`m a Python program')
    print(greeting)


greet(bark)


def whisper(text):
    return text.lower() + '...'


greet(whisper)


# Map with functions
print(list(map(bark, ['hello', 'hey', 'hi'])))


# Functions can be Nested

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


print(speak('Hello, World'))


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell

    else:
        return whisper


speak_func = get_speak_func(0.7)
print(speak_func('Hello'))


# Functions can capture local state
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell

    else:
        return whisper


print(get_speak_func('Hello, World', 0.7)())


# Pre-configure

def make_adder(n):
    def add(x):
        return x + n
    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4), plus_5(4))


# Objects can behave like functions

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
print(plus_3(4))
