# 这是一个模块例子

name = 'Bob'
age = 24
dict01 = {'name':'Bob', 'age':24}


def exam():
    print('模块函数例子')


class Cat:
    def __init__(self):
        """初始化方法"""
        # _init_初始化主要用来初始化数据
        # 初始化属性数据
        # 在使用类模板创建对象时自动调用
        print("1.初始化属性")
        # 在类内部添加属性  self.属性名 = 属性初始值
        self.name = "小花"

    def eat(self):
        print("--%s爱吃鱼--" % self.name)


