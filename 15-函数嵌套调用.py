def demo2():
    print("函数1---------01")
    print("函数1---------02")

def demo1():
    print("函数2----------01")
    demo2()    # 调用函数
    print("函数2----------02")

demo1()