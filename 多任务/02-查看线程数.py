import threading
import time


def test1():
    for i in range(5):
        print("---test1---%d" % i)
        time.sleep(1)


def test2():
    for i in range(10):
        print("---test2---%d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)  # target = 函数名,相当于创建一个Thread对象
    t2 = threading.Thread(target=test2)

    t1.start()    # 线程的执行是没有顺序的
    # time.sleep(1)

    t2.start()  # 启动线程
    # time.sleep(1)
    while True:
        print(threading.enumerate())  # 返回一个包含正在运行的线程的list,mainthread 表示主线程，thread是子线程
        if len(threading.enumerate()) <=1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
