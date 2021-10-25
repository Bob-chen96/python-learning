from threading import Thread
from time import time, sleep
from random import randint

"""
target：通过 target 参数传入一个函数名来表示进程启动后要执行的代码
args：是一个元组，代表传递给函数的参数列表
start：Process 的 start() 方法来启动进程
join：Process 的 join() 方法表示等待进程执行结束，才会往下执行
"""
def download_file(filename):
    print(f"开始下载{filename}------")
    download_time = randint(2,10)
    sleep(download_time)
    print(f"{filename}下载完成，用了{download_time}s")

def main():
    start = time()
    p1 = Thread(target=download_file, args=('python开发.doc',))
    p2 = Thread(target=download_file, args=('安卓开发.pdf',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f"总共耗时{end - start}s")

if __name__ == '__main__':
    main()
