"""
程序：一个程序是一个静态的
进程：一个程序运行后，代码+所用的资源叫进程，是系统分配资源的基本单位
"""


import time
import multiprocessing  # 导入进程模块


def test1():
    while True:
        print("1------")
        time.sleep(1)


def test2():
    while True:
        print("2------")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    p1.start()
    p2.start()       # 实现多进程多任务


if __name__ == "__main__":
    main()

