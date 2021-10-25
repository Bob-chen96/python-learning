import time
from collections.abc import Iterable
from collections.abc import Iterator

a = isinstance([11, 22, 33], Iterable)
# 判断一个对象是否可以迭代
print(a)


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个可以迭代的对象，即可以用for，那么必须实现__iter__方法"""
        # return ClassIterator()
        # # 返回对象是一个类对象，有iter和next方法，是一个迭代器
        return self   # return 哪个对象，就调用它的__next__方法

    def __next__(self):
        if self.num < len(self.names):
            ret = self.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration  # 抛出一个结束异常，退出程序


# class ClassIterator(object):
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         return 1


classmate = Classmate()
# print(isinstance(classmate, Iterable))  # 判断对象是否可迭代
#
# classmate_iterator = iter(classmate)  # iter（类对象）函数返回一个迭代器
# print(classmate_iterator)
# print(isinstance(classmate_iterator, Iterator))  # 判断是否为迭代器

classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

for temp in classmate:   # 这里调用的是类对象的next返回值,每次都会调用next函数
    print(temp)
    time.sleep(1)


