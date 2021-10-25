""" @classmethod      @classmethod 是装饰器，对函数或方法进行装饰
 def 类方法(cls):
     pass
"""


class Person:
    count = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃方法")

    # 是装饰器，高速py解释器这是个类方法
    @classmethod
    def get_count(cls):
        """类方法"""
        print("类方法作用：处理类属性或调用其他类方法")
        print("cls参数保存的是当前类对象的引用，cls:", cls)  # cls 这里相当于类对象
        cls.count += 10
        return cls.count


print(Person)

# 调用类方法： 类对象.类方法名（）
ret = Person.get_count()
print(ret)