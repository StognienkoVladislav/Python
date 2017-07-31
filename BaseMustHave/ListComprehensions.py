from scipy._lib.six import xrange

if __name__ == '__main__':

    res = []

    for x in xrange(1, 25, 2):
        res.append(x)

    print(res)

    #######################################################

    res = [x for x in range(1, 25, 2)]
    print(res)

    res = [x ** 2 for x in range(1, 25, 2) if x % 3 != 0]
    print(res)

    dic = {'John' : 1200, 'Paul' : 1000, 'Jones' : 1850, 'Dorothy' : 950}
    print ("\n".join(["%s = %d" % (name, salary) for name, salary in dic.items()]) )

    #######################################################

    #1 считываем из файла строки и делим их на пары IP - адрес
    raw = [x.split(" ") for x in open("ipBytes.txt")]

    #2 заполн словарь
    rmp = {}
    for ip, traffic in raw:
        if ip in rmp:
            rmp[ip] += int(traffic)

        else:
            rmp[ip] = int(traffic)


    #3 переводим в список
    lst = rmp.items()

    #4 получ результат
    print("\n".join(["%s\t%d" % (host, traff) for host, traff in lst]))


