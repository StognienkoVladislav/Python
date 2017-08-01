
import functools

def foo():
    print("foo")


def bar(func):
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

######################################################

def bar2(func):
    #Обьявляем "wrapper" оборачивающим "func"
    #и запускаем
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar2
def foo():
    print("foo")



if __name__ == '__main__':
    print(foo.__name__)
    print(foo.__name__)