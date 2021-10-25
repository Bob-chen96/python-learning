# _del_方法：当前程序退出时，对象从内存空间销毁前，自动调用
class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)
    # 局部变量作用范围只能是当前方法，如果想让下面的方法访问到当前变量
    # 需要把局部变量保存为属性
        self.file = open("1.txt", "w", encoding="utf-8")
        self.file.write([1, 2])
        self.file.close()

    def __del__(self):
        """删除魔法方法"""
        print("当前程序退出时，对象从内存空间销毁前，自动调用")
        print("清除资源的操作")
        print("文件关闭前---")
        self.file.close()  # 无论上面程序是否崩溃，都可以执行
        print("文件关闭后---")

        # 对象的生命周期：从使用类模板开始，到调用_del_方法结束


tom = Cat("汤姆猫")
tom.eat()

# 注意：_def_方法在程序退出之前自动调用
del tom  # 手动调用，对象内存空间被销毁

