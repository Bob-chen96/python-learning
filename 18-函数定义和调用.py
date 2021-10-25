def hello():
    '''
    这里是函数文档注释
    :return:
    '''
    print("hello world!")
    return 2   # return 可以将函数运行结果返回到函数调用的地方

hello()

help(hello)  # help(函数名) 查看函数注释

#函数调用顺序：
#1.函数定义时，不会进入函数内部代码
#2.调用函数时，才会进入函数内部执行代码
#3.调用函数完成后，回到函数调用的地方继续向下执行

info = hello()
print(info)