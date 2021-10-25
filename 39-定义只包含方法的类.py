"""语法格式:定义一个只包含方法的类
class 类名:
    def 方法1（self, 参数列表）：
        pass
    def 方法2（self, 参数列表）：
        pass
"""
# 定义类模板
class Person:
    # 当定义方法时，自动添加self参数
    print("--扫描--")
    def run(self):
        print("跑方法")
    def eat(self, food):
        print("吃%s" %food)


# 创建对象
# 格式： 对象变量 = 类名()
xiao_ming = Person()  # 定义类模板时，会进入类模板扫描一次，定义方法不会进入内部执行代码
print(xiao_ming)  # 输出地址，对象名就是一个变量名保存当前内存空间的引用地址

# 通过对象来调用方法
# 格式：对象变量名.方法名（）   调用方法时，self参数不需要我们传递
# 类的三大特性之一就是可以封装函数
xiao_ming.run()
xiao_ming.eat("饭")