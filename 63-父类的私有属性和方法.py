class Father:
    """父类"""
    def __init__(self):
        self.name = "Bob"
        # 私有属性
        self.__password = 9527

    # 在类的内部对外提供访问私有属性的接口 get/set
    def get_pwd(self):
        return self.__password

    def func_pwd(self):
        """调用私有方法"""
        self.__secret()

    def eat(self):
        print("%s 爱吃东西" % self.name)

    def __secret(self):
        """私有方法"""
        print("%s 的银行卡密码密码是：%d" % (self.name, self.__password))


class Son(Father):
    """子类"""
    def run(self):
        print("小王爱跑步..")


xiao_wang = Son()
xiao_wang.eat()

# 在类外，子类对象无法直接访问父类私有方法
print(dir(xiao_wang))

xiao_wang.get_pwd()
xiao_wang.func_pwd()