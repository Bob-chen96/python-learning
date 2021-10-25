"""
完整格式：
try:
    尝试执行的代码
except 错误类型1：
    处理代码
    pass
except （错误类型2， 错误类型3）：
    处理代码
    pass
except Exception as result：
    错误处理
    print（result）
else:
    没有异常才会执行的代码
    pass
finally：
    有没有异常，都会执行的代码

"""
try:
    num = 1
    print(num)
    print(1111)    # try有多个异常，只会捕获第一个异常，后面代码不会执行
except (NameError, FileNotFoundError) as Error:  # 一次捕获多个异常,别名保存了错误信息
    print("捕获姓名错误异常，错误信息：", Error)   # 只要捕获了异常，try部分无论有没有异常，程序都可以正常结束，只有发生异常才会输出
except ValueError:
    print("捕获到值错误异常")
except Exception:
    print("捕获到任意类型异常")  # 当上面错误类型都没有时，会执行Exception部分
else:
    print("try部分没有错误，就会执行")
finally:
    print("无论有没有异常，都会执行")
print("继续")

# 应用场景，在打开文件向文件写入数据时程序崩溃
# 此时可在finally添加文件关闭操作，避免系统资源浪费
