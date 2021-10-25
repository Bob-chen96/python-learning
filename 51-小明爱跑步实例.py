class Person:
    """人类"""
    def __init__(self, name, weight):
        """初始化方法"""
        self.name = name
        self.weight = weight

    def __str__(self):
        """打印对象描述信息"""
        return "姓名是:%s 体重是:%.2f公斤" % (self.name, self.weight)

    def run(self):
        """跑方法"""
        print("%s 爱跑步，每次跑步减肥0.5公斤" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃方法"""
        print("%s 爱吃东西，每次吃东西，体重增加1公斤" % self.name)
        self.weight += 1

Bob = Person("鲍勃",60.5)
print(Bob)

Bob.run()
print(Bob)

Bob.eat()
print(Bob)

# 属性都是添加到对象的内存空间中，self保存当前对象的引用地址
