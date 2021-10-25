import threading
import time

# 定义一个全局变量
g_num = 100
g_nums = [11, 22]


def test1(temp):
    global g_num
    g_num += 1
    temp.append(33)
    print("---in test1 g_num = %d----" % g_num)
    print("---in test1 temp = %s---" % str(temp))


def test2():
    print("---in test2 g_num = %d" % g_num)


def main():
    # target 指定这个线程取哪个函数执行代码
    # args指定调用函数的时候 传递什么参数过去，是一个元组
    t1 = threading.Thread(target=test1, args=(g_nums,))  # 子线程和子线程之间共享全局变量
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main thread g_num = %d" % g_num)


if __name__ == "__main__":
    main()