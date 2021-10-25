"""
并行：真的多任务，多核CPU
并发：假的多任务
"""
import time
import threading    # 导入线程模块


def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("---唱歌ing---")
        time.sleep(1)


def dance():
    """跳舞5秒钟"""
    for i in range(5):
        print("---跳舞ing---")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


main()

