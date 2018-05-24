import random
import sys


def epidemic(n, i):
    # done_checker - счетчик для успешных передач данных всем нодам
    done_checker = 0
    for _ in range(i):
        """
        mass - изначальный нулевой массив нод
        workers - ноды, в которых есть хотя бы 1 пакет (изначально данные передаються с ноды с индексом 0)
        X - кол-во рандомных узлов
        """
        mass = [0]*n
        workers = [0]
        X = 4
        iterr = 0
        # пока есть не залоченные ноды
        while workers:
            iterr += 1
            # check - нода, от которой рандомно передаютсья X пакетов другим нодам
            check = workers.pop(0)
            # При mass[check] == 2, нода закрываеться
            if mass[check] <= 1:
                mass[check] += 1
            else:
                continue
            for _ in range(X):
                iterr += 1
                # Рандомно выбираем Х-кол-во нод, которым передадим данные, исключая текущую ноду
                r = random.choice([x for x in range(len(mass)) if x != check])
                # Добавляем их для следующих итераций
                workers.append(r)
        # Если сумма значенний в массиве равна 2*N(кол-во нод), то все ноды закрыты
        # инкрементируем счетчик
        print("Кол-во итераций: {}".format(iterr))
        if sum(mass) == 2*n:
            done_checker += 1
    # Процент успешных передач
    print('In {}% cases all nodes received the packet'.format((done_checker/i)*100))


if __name__ == '__main__':
    epidemic(20, 10)
    # epidemic(int(sys.argv[1]), int(sys.argv[2]))
