

if __name__ == '__main__':

    #Перечисление
    iterable = range(1, 25)
    i = 0
    for item in iterable:
        print (i, item)
        i += 1

    for i, item in enumerate(iterable):
        print(i, item)

    print(list(enumerate('abc')))
    print(list(enumerate('abc', 1)))

    print('\n########################################\n')

    #Абстракция словарей/множеств
    my_dict = {i : i * i for i in range(100)}
    my_set  = {i * 15 for i in range(100)}


    #простой сервер
    #python 2
    #python -m SimpleHTTPServer

    #python 3
    #python3 -m http.server
    #Эта команда запустит сервер


    #Вычисление выражений Python
    import ast
    expr = "[1, 2, 3]"
    my_list = ast.literal_eval(expr)        #Выкидывает exception , если данные не валидны
    print(my_list)

    #А не так
    expr = "[1, 2, 3]"
    my_list = eval(expr)
    print(my_list)

    #Интроспекция обьектов
    foo = [1, 2, 3, 4]
    print(dir(foo))     #Изучение обьекта


    #Отладочный скрипт
    import pdb
    pdb.set_trace()

    #pdb.set_trace()    Задает точку останова в любом месте скрипта

    #Упрощенная конструкция if
    if n in [1, 4, 5, 6]:
        pass

    #вместо
    if n == 1 or n == 4 or n == 5 or n == 6:
        pass

    #Разворачивание списка/строки
    a = [1, 2, 3, 4]
    print(a[::-1])  #это создает новый разверн список
    a.reverse()     #развернуть имеющийся

    #То же самое и со строкой

    #Красивый вывод
    from pprint import pprint
    pprint(my_dict)

    #Так же можно выводить инфу с JSON
    cat file.json | python -m json.tool

    #Тернарный оператор
    [on_true] if [expression] else [on_false]
    x, y = 50, 25

    small = x if x < y else y


