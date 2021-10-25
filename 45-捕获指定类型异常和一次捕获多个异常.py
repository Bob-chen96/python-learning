try:
    # num = 1
    print(num)
    print(1111)    # try有多个异常，只会捕获第一个异常，后面代码不会执行
except (NameError, FileNotFoundError):  # 一次捕获多个异常
    print("捕获姓名错误异常")   # 只要捕获了异常，try部分无论有没有异常，程序都可以正常结束，只有发生异常才会输出
except ValueError:
    print("捕获到值错误异常")
# 只会执行对应类型异常的输出
print("继续")

# 异常类型：报错最后一行的第一个单词
