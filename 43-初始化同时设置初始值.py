class Dog:
    def __init__(self, name):
        # 在内部使用 self.属性 = 形参 接受外部传递的参数
        self.name = name

    def sleep(self):
        print("--%s在睡觉" % self.name)


Tom = Dog("旺财") # 这里创建对象时要带入参数
Tom.sleep()
