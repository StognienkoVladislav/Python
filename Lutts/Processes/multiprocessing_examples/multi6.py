#пулы процессов

import os
from multiprocessing import Pool

def powers(x):
    #print(os.getpid())      #чтоб увидеть работу потомков
    return 2**x

if __name__ == '__main__':
    workers = Pool(processes=5)

    result = workers.map(powers, [2]*100)
    print(result[:16])
    print(result[-2:])

    result = workers.map(powers, range(100))
    print(result[:16])
    print(result[-2:])


