class T(object):
    """abbababbababba"""
    def __str__(self):
        return "100"

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


# 类名.__doc__获取描述信息
print(T.__doc__)

# __module__表示当前操作的对象在哪个模块
# __class__表示当前操作的对象的类是什么
obj = T()
print(obj.__module__)
print(obj.__class__)

# __dict__ 检查类或对象的所有属性
print(obj.__dict__)

# __str__,如果在类中定义了一个该方法，那么打印对象时，默认输出该方法的返回值
# print(obj)

# __getitem__,__setitem__,__delitem__方法用于索引操作，如字典
result = obj['k1']  # 触发第一个方法
obj['k2'] = '111'  # 触发第二个方法
del obj['k1']  # 触发第三个方法
