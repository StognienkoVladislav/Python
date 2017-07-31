import urllib


if __name__ == '__main__':

    #Tuple
    #Используется для представления неизменяемой последовательности разнородных объектов.

    t = (2, 2.05, "Hello")
    print(t)

    (a, b, c) = t
    print(a, b, c)

    z, y, x = t
    print(z, y, x)

    a = 1
    b = 2
    a, b = b, a

    x = 12,
    print(x)

    ########################################################################################

    #List

    a = [2, 2.25, "Python"]
    print(a)

    b = list("help")
    print(b)

    c = [x ** 3 for x in range(20) if x % 2 == 1]
    print(c)

    ########################################################################################

    s = [0, 1, 2, 3, 4]
    print (s[0], s[-1], s[3])

    s[2] = -2
    print(s)

    del s[2]
    print (s)

    ########################################################################################
    #Срезы

    l = range(12)
    print(l)

    print(l[1:3], l[-1:], l[::2])

    l[0: 1] = [-1, -1, -1]
    print(l)

    del l[:3]
    print(l)

    ########################################################################################

    #Словари
    h1 = {1 : "one", 2 : "two", 3 : "three"}
    h2 = {0 : "zero", 5 : "five"}
    h3 = {"z" : 1, "y" : 2, "x" : 3}

    for key, value in h1.items():
        print(key, " ", value)

    for key in h2.keys():
        print (key, " ", h2[key])

    for v in h3.values():
        print (v)

    #Добавл элементов из другого хеша
    h1.update(h3)

    #Кол-во пар в хеше
    print (len(h1))

    ########################################################################################
    #File

    #Копир файла
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt", "w")

    for line in f1.readlines():
        f2.write(line)

    f2.close()
    f1.close()

    #Через url
    f1 = urllib.urlopen("hhtp://python.onego.ru")

