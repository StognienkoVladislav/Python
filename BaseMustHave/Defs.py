

def safe_div(x, y):

    """For fun and profit"""

    if y != 0:
        z = x // y
        print (z)
        return z

    else:
        print("Yippie-kay-yay")

def gcd(a, b):
    "Нахождение НОД"
    while a != 0:
        a, b = b%a, a
    return b

#position-arguments

def list_sum(*args):
    smm = 0
    for arg in args:
        smm += arg

    return smm



if __name__ == '__main__':

    print(safe_div.__doc__)
    mystic_function = safe_div
    print(mystic_function(10, 4))

    print(list_sum(1, 2, 3))
    print(list_sum(1))

    lst = [1, 10, 2]

    print(list(range(*lst)))

    
