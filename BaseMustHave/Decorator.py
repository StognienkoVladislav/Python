
def my_shiny_new_decorator(function_to_decorate):
    #Внутри себя декоратор определяет функцию - "обертку"
    #Она будет обернута вокруг декорируемой
    #получ возможность исполнять произв код до и после нее

    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функц
        print("А я - код, срабатывающий после")
    # Вернём эту функцию

    return the_wrapper_around_the_original_function

    # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.

def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")


@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


################################################################################

def bread(func):
    def wrapper():
        print()
        func()
        print("<\________/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~слата~")
    return wrapper

def sandwich(food = "--ветчина--"):
    print(food)


@bread
@ingredients
def sandwich(food = "--ветчина--"):
    print(food)

###########################################################

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_nmae(first_name, last_name):
    print("Маня зовут", first_name, last_name)

###########################################################

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)

    return wrapper

class Lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))

###########################################################


if __name__ == '__main__':

    stand_alone_function()

    # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
    # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,

    # готовую к использованию функцию:
    #stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
    #stand_alone_function_decorated()

    stand_alone_function = my_shiny_new_decorator(stand_alone_function)
    stand_alone_function()


    print("##########################################")
    another_stand_alone_function()
    print("##########################################")

    #######################################################

    sandwich()

    sandwich = bread(ingredients(sandwich))
    sandwich()

    #######################################################

    print_full_nmae("Random", "qwerty")

    #######################################################

    l = Lucy()
    l.sayYourAge(-3)
