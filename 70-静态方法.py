"""
语法：
@staticmethod
def 静态方法名():
    pass
"""


class Person:
    count = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃方法")

     # 是装饰器，告诉我们这是个静态方法
    @staticmethod
    def func_static():
        """静态方法"""
        print("静态方法中不用self参数，也不要cls参数")
        print("静态方法不需要实例属性和方法")

    @staticmethod
    def sum(a, b):
        return a + b


# 调用静态方法
# 1.类名.静态方法名
Person.func_static()

# 2.实例对象.静态方法名
a = Person.sum(1, 2)  # 静态方法可以有参数
print(a)