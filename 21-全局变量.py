# 在所有函数外定义的变量就是全局变量
g_num = 200

def ex1():
    global g_num  # 在函数内修改全局变量，要加上global关键字
    g_num = 300   # global告诉解释器修改的是全局变量
    print("全局变量=%d" % g_num)

def ex2():
    print("全局变量=%d" % g_num)  # 修改后其他的全局变量也会一同改变

ex1()
ex2()