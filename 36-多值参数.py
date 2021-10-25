# *args用来接收多余参数，以元组格式保存
# **kwargs用来接收多余关键字参数，以字典格式保存
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(10, 20, 30, name="张三", age=10)

