errno = 50159747054
name = 'Bob'
err_message = 'Hey Bob, there is a 0xbadc0ffee error!'


# Old formatting
print('Hello, %s' % name)
print('%x' % errno)

print('Hey %s, there is a 0x%x error!' % (name, errno))

print('Hey %(name)s, there is a 0x%(errno)x error!' % {
      "name": name, "errno": errno})


# New style formatting
print('Hello, {}'.format(name))

print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))


# Literal String Interpolation (Python 3.6+)
print(f'Hello, {name}!')

a = 5
b = 10
print(f'Five plus ten is { a + b } and not {2*(a + b)}.')


def greet(name, question):
    return f'Hello, {name}! How`s it {question}?'


greet('Bob', 'going')

print(f"Hey {name}, there's a {errno:#x} error!")


# Template Strings

from string import Template

t = Template('Hey, $name!')
print(t.substitute(name=name))

templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(
    name=name, error=hex(errno)
))



############################3

SECRET = 'this-is-a-secret'


class Error:
    def __init__(self):
        pass


err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))

user_input = '${error.__init__.__globals__[SECRET]}'
print(Template(user_input).substitute(error=err))
# Error
