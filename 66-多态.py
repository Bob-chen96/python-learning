"""
多态：不同的子类对象调用相同的父类方法，产生不同的执行结果
成立的三个条条件：
1.要有继承
2.要有方法的重写
3.要有父类的对象或子类的对象作为方法的参数
"""


class Dog:
    """普通狗类"""
    def __init__(self, name):
        self.name = name

    def game(self):
        print("普通狗只是简单的玩耍")


class XiaoTianQuan(Dog):
    """哮天犬类"""
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在天上玩耍" % self.name)


class Person:
    """人类"""
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("人物：%s 和狗对象：%s 一起玩耍" % (self.name, dog.name))
        # 狗对象调用game方法，用对象作为函数参数
        dog.game()


# 普通狗类创建对象
lai_fu = Dog("来福")

# 哮天犬类创建对象
xtq = XiaoTianQuan("哮天犬")

# 使用人类模板创建对象
chang_wei = Person("常威")

# 调用和狗玩的方法
chang_wei.play_with_dog(lai_fu)
chang_wei.play_with_dog(xtq)
