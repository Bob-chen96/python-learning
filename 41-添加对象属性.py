# 给对象添加属性：
# 1.类的外部添加：  对象名.属性名 = 属性值

class Person:
    # 当定义方法时，自动添加self参数
    print("--扫描--")
    def run(self):
        print("跑方法-----self:", self)
        print("%s在跑步" % self.name)


    def eat(self, food):
        print("%s吃%s---" % (self.name, food))
        # 在类内部通过self参数访问属性  self.属性名
        print("---self:", self)
        self.run()
        # 内部访问方法 self.方法名（参数）


Bob = Person()
# 在类外添加对象属性
print(Bob)

Bob.name = "帅哥"

Bob.eat("饭")
Bob.run()

