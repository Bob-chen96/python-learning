class Women:
    def __init__(self, name):
        self.name = name
        # 前置双下划线的属性是私有属性
        self.__age = 20

    # 对外提供访问私有属性的接口（方法） get/set
    def get_age(self):
        return self.__age

    def eat(self):
        print("%s 是一个吃货，近年%d" % (self.name, self.__age))
        self.__secret()
        # 私有方法和私有属性只能在类内部使用

    def __secret(self):
        # 前置双下划线的方法时私有方法
        print("个人秘密，不方便透露..")


Sue = Women("小仙女")
# print(Sue._age)  # 在类的外部无法直接访问私有属性
# Sue._secret()  # 在类的外部无法直接访问私有方法
Sue.eat()

# py中没有真正意义上的私有，是通过名字重整的方式，把私有属性和方法改了名字
# __私有属性名/方法  改成 _类名__私有属性/方法

# print(Sue._Women__age)
# Sue._Women__secret()