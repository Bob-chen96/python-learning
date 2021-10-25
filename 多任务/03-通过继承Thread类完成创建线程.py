import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + str(i)
            print(msg)


if __name__ == "__main__":
    t = MyThread()   #  创建一个实例对象，只会有一个线程执行
    t.start()