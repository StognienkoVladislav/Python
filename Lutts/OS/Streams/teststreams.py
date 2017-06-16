#Читает числа до символа конца файла и выводит их квадрат

def interact():
    print('Hello stream world')         #print выводит в sys.stdut
    while True:
        try:
            reply = input('Enter a number>')    #input читает из sys.stdin

        except EOFError:
            break

        else:
            num = int(reply)
            print("%d squared is %d" % (num, num**2))

        print('Bye')

if __name__ == '__main__':
    interact()