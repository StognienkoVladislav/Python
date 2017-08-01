
#Максимально общий декоратор

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    #Данная "обертка" принимает любые аргументы

    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_arguments():
    print("Python is cool, no argument here.")


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus = "Почему нет?"):
    print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))

class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie = -3):         #знач по умолчанию
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))

###############################################################################

#Декоратор, принимающий аргументы
def decorator_maker():
    print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")

    def my_decorator(func):
        print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
        def wrapped():
            print("Я - обёртка вокруг декорируемо функции. \n"
                  "Я буду вызвана каждый раз, когда ты вызваешь декор функцию.\n"
                  "Я возвращаю результат работы декорируемой функции.")
            return func()
        print("Я возвращаю обёрнутую функцию.")
        return wrapped
    print("Я возвращаю декоратор.")
    return my_decorator


def decorated_function():
    print("Я - декорируемая функция.")


@decorator_maker()
def decorated_function():
    print("Я - декорируемая функция.")


if __name__ == '__main__':


    function_with_no_arguments()
    function_with_arguments(1, 2, 3)
    function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
    m = Mary()
    m.sayYourAge()

    ###########################################################################

    new_decorator = decorator_maker()
    decorated_function = new_decorator(decorated_function)
    #Теперь вызовем функцию
    decorated_function()

