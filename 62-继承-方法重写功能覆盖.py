# 重写：子类中有与父类相同的方法名，子类重写了父类的方法
# 分类：1.功能覆盖：子类重写的方法与父类完全不同
#      2.功能扩展


class Cat:
    """猫类"""
    def catch(self):
        print("小猫抓老鼠")


class Bosimao(Cat):   # 单继承  子类（父类）
    """波斯猫类"""
    def catch(self):
        # 在子类中调用父类方法，进行功能扩展
        # 1.super().重写的方法名
        # super().catch()
        # 2.父类名.方法名（self）,不推荐
        Cat.catch(self)
        print("波斯猫会抓鱼")


bsm = Bosimao()
bsm.catch()   # 子类会调用自己的方法，功能覆盖


