# *args是非关键字参数，用于元组，**kw是关键字参数，用于字典
# 装饰器可以在不改动原函数代码的情况下，添加其原本没有的功能


def loop(func):
    def wrapper(*args, **kw):
        for i in range(2):
            func(*args, **kw)
    return wrapper


def test():
    print("输出一次")


# 1.第一种方法
loop(test)()


# 第二种方法
@loop
@loop
@loop
def test2():
    print("再次输出1次")
# 上述代码就相当于：loop(loop(loop(test)))()，真正调用的是最外面那层。
test2()


def times(times):
    def decorator(func):
        def wrapper(*args, **kw):
            for i in range(times):
                func(i, **kw)
        return wrapper
    return decorator


@times(10)
def test3(num):
    print(f"第{num}次打印")

test3()

"""而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。

如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。
下面上代码。

"""
class A(object):
    bar = 1
    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(cls.bar)
        cls().foo()
###执行
A.static_foo()
A.class_foo()
