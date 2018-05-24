import random
import sys


def algor(n, i):
    # done_checker - счетчик для успешных передач данных всем нодам
    done_checker = 0

    for _ in range(i):
        """
        ultra_check - массив с нодами, которые получили 1 пакет
        mass - изначальный нулевой массив нод
        X - кол-во рандомных узлов
        iterr - кол-во итераций в циклах
        """
        ultra_check = []
        mass = [0]*n
        X = 2
        iterr = 0

        # Пока все ноды не получат пакет данных
        while len(ultra_check) != len(mass):
            iterr += 1
            for _ in range(X):
                iterr += 1
                # Рандомно выбираем Х-кол-во нод, которым передадим данные, исключая текущую ноду
                try:
                    r = random.choice([x for x in range(len(mass)) if x not in ultra_check])
                    mass[r] = 1
                    ultra_check.append(r)
                # Если все ноды уже заполненны и не кому передавать данные - выходим из цикла
                except:
                    break
        print("Кол-во итераций: {}".format(iterr))
        # Если сумма значенний в массиве равна N(кол-во нод), то все ноды закрыты
        # инкрементируем счетчик
        if sum(mass) == n:
            done_checker += 1

    print('In {}% cases all nodes received the packet'.format((done_checker / i) * 100))

    """
    Возможно я не так понял задание:
    <<Вторым обязательным условием является написать алгоритм пересылки 
    пакета который хотя бы на 1% лучше, и продемонстрировать это:>>
    В мое случае, нода выбирает исключительно ту ноду, которой еще не передавался пакет и нет
    возможности закрытия другой ноды(т.к. одной и той же не передаеться пакет данных)
    """


if __name__ == '__main__':
    algor(20, 10)
    #algor(int(sys.argv[1]), int(sys.argv[2]))
