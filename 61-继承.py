# 继承：子类拥有父类所有方法和属性
# 优点：1.实现代码的重用 2.简化代码的结构

"""
继承语法：
class 类名（父类名）：
    pass

子类继承父类
"""
# 实现单继承
class Animal:
    """动物类"""
    def __init__(self):
        self.name = "动物"
        self.age = 2

    def eat(self):
        print("%s 爱吃东西" % self.name)


class Cat(Animal):     # 单继承  子类（父类）
    """猫类"""
    def catch(self):
        print("小猫抓老鼠")


class Bosimao(Cat):
    """波斯猫类"""
    def sing(self):
        print("波斯猫会唱歌")

# 父类对象无法调用子类方法,子类对象可以调用父类的方法
Tom = Cat()
print(Tom.name)
Tom.eat()

bsm = Bosimao()
print(bsm.name)
bsm.eat()    # 孙子类对象可以调用父类和爷爷类方法

# 继承不是复制，访问子类属性时，先到子类中查找，没有再去父类中查找