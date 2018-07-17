
import threading


x = 0


def increment_global():
    global x
    x += 1


def task_of_thread(lock):

    for _ in range(50000):
        lock.acquire()
        increment_global()
        lock.release()


def main():
    global x
    x = 0

    lock = threading.Lock()
    t1 = threading.Thread(target=task_of_thread(lock))
    t2 = threading.Thread(target=task_of_thread(lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    for i in range(5):
        main()
        print("x={} after Iteration {}".format(x, i))
