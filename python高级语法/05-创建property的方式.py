# 第一种方法
class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    # 设置方法
    @price.setter
    def price(self, value):
        self.original_price = value

    # 删除方法
    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
obj.price   # 调用第一个函数
obj.price = 200  # 调用第二个函数
del obj.price  # 调用第三个函数


# 第二种方法

class Foo:
    def get_bar(self):
        print("get方法")
        return "111"

    def set_bar(self, value):
        print("set方法")
        return value

    def del_bar(self):
        print("deleter方法")
        return "222"

    BAR = property(get_bar, set_bar, del_bar, "描述")


obj = Foo()
obj.BAR  # 调用第一个方法
obj.BAR = 'wisji'  # 调用一二个方法
del obj.BAR  # 调用第三个方法
desc = Foo.BAR.__doc__  # 输出描述部分
print(desc)

