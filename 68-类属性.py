class Person:
    # 类属性，定义在方法外边，类的内部
    # 作用，记录类对象的相关特征
    count = 0   # 类属性只会初始化一次
    print("---初始化一次")

    def __init__(self, name):
        # 实例属性
        self.name = name
        print("---初始化方法__init__")
        # 访问类属性，使用类名.类属性
        Person.count += 1

    def eat(self):
        print("吃方法")


xiao_ming = Person("小明")
# 类外访问类属性方式：1.类名.类属性名（推荐）   2.实例对象.类属性名
print(Person.count)
# 通过类名.类属性 = 值 可以修改属性值

xiao_wang = Person("小王")
print(xiao_wang.count)
