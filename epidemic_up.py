import random
import sys


def algor(n, i):
    checker = 0

    for _ in range(i):
        ultra_check = []
        mass = [0]*n

        X = 2

        while len(ultra_check) != len(mass):

            for _ in range(X):
                try:
                    r = random.choice([x for x in range(len(mass)) if x not in ultra_check])
                    mass[r] = 1
                    ultra_check.append(r)
                except:
                    break

        if sum(mass) == n:
            checker += 1

    print((checker/i)*100)


if __name__ == '__main__':
    # algor(20, 1000)
    algor(int(sys.argv[1]), int(sys.argv[2]))
