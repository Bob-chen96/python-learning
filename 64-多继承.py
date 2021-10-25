"""
格式：
class 类名（父类名1， 父类名2.....）
    pass
"""


class Horse:
    """马类"""
    def run(self):
        print("马跑得快")

    def walk(self):
        print("马走不远")


class Donkey:
    """驴类"""
    def walk(self):
        print("驴会走路")

    def run(self):
        print("驴跑不快")


class Mule(Horse, Donkey):
    """骡子类"""
    pass


# 多继承中，子类可以访问所有父类的属性和方法，不包括私有
mu = Mule()
mu.run()
mu.walk()

# __mro__ 方法解析顺序,查看类的方法执行顺序
print(Mule.__mro__)

# 多继承，父类有相同方法名，参考__mro__方法解析顺序来调用
# 如果找到了，就调用其中的方法，没找到找下一个类中的方法