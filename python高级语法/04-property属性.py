class Goods:
    def func(self):
        pass

    # 定义property属性,不能有参数
    @property
    def size(self):
        return 100


obj = Goods()
# 调用property属性不用加括号,类似于调用实例属性
ret = obj.size
print(ret)