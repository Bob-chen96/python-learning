"""
_str_方法：
特点：打印对象时，自动调用 print(对象名) _str_()方法自动调用
作用：打印对象的描述信息
注意：必须有返回值，只能返回字符串
"""

class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def __str__(self):
        """对象描述信息方法"""
        print("使用print方法时，打印对象时，自动调用")
        return "名字是%s" % self.name   #只能返回字符串

Lion = Cat("大脸猫")
print(Lion)  #  打印对象引用地址，添加_str_方法后，会打印返回值