class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃方法")

# 创建的对象在内存空间实际存在，叫实例对象


xiao_ming = Person("小明")
print(xiao_ming)
print(xiao_ming.name)  # 实例对象的属性是实例属性
xiao_ming.eat()  # 实例对象的方法时实例方法

# 类名就是一个变量名，也是一个对象，保存类对象的引用地址，py中一切皆对象
print(Person)
print(id(Person))