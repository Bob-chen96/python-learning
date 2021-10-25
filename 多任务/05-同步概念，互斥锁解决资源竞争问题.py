""" threading模块中有Lock模块
    创建一个互斥锁 mutex = threading.Lock()

"""
import threading
import time

# 定义一个全局变量
g_num = 0
# 创建一个互斥锁,默认没有上锁
mutex = threading.Lock()


def test1(temp):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前已经被上锁了，那么此时会堵塞在这里，直到这个锁被解开为止
    mutex.acquire()
    for i in range(temp):
        g_num += 1
    # 解锁
    mutex.release()
    print("---in test1 g_num = %d----" % g_num)


def test2(temp):
    global g_num
    mutex.acquire()  # 加锁
    for i in range(temp):
        g_num += 1
    mutex.release()
    print("---in test2 g_num = %d" % g_num)


def main():
    # target 指定这个线程取哪个函数执行代码
    # args指定调用函数的时候 传递什么参数过去，是一个元组
    t1 = threading.Thread(target=test1, args=(10000,))  # 子线程和子线程之间共享全局变量
    t2 = threading.Thread(target=test2, args=(10000,))

    t1.start()

    t2.start()

    print("---in main thread g_num = %d" % g_num)


if __name__ == "__main__":
    main()