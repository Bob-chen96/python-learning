try:
    # num = 1
    print(num)
    print(1111)    # try有多个异常，只会捕获第一个异常，后面代码不会执行
except (NameError, FileNotFoundError) as Error:  # 一次捕获多个异常,别名保存了错误信息
    print("捕获姓名错误异常，错误信息：", Error)   # 只要捕获了异常，try部分无论有没有异常，程序都可以正常结束，只有发生异常才会输出
except ValueError:
    print("捕获到值错误异常")
except Exception:
    print("捕获到任意类型异常")  # 当上面错误类型都没有时，会执行Exception部分
print("继续")



# 异常类型：报错最后一行的第一个单词
