import random
import sys


def algor(n, i):
    checker = 0
    for _ in range(i):
        mass = [0]*n
        # print(mass)

        workers = [0]

        X = 3

        while workers:

            check = workers.pop(0)
            if mass[check] <= 1:
                mass[check] += 1
            else:
                continue
            for _ in range(X):
                r = random.choice([x for x in range(len(mass)) if x != check])
                workers.append(r)
        if sum(mass) == 2*n:
            checker += 1

    print((checker/i)*100)


if __name__ == '__main__':
    algor(20, 1000)
    # algor(int(sys.argv[1]), int(sys.argv[2]))
