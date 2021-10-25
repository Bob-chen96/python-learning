import threading
import time


def test1():
    for i in range(2, 101):
        j = 2
        while i % j != 0:
            j = j+1
        if j == i:
            print(i)
            time.sleep(1)


def test2():
    for i in range(2, 101):
        j = 2
        while i % j != 0:
            j = j+1
        if j == i:
            print(i)
            time.sleep(1)


def test3():
    for i in range(2, 101):
        j = 2
        while i % j != 0:
            j = j+1
        if j == i:
            print(i)
            time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t3 = threading.Thread(target=test3)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    t3.start()
    time.sleep(1)


if __name__ == "__main__":
    main()