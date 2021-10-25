nums = [x*2 for x in range(10)]
print(nums)  # 返回列表

num = (x*2 for x in range(10))
print(num)  # 返回的是生成器（一种特殊的迭代器）


def fibo_num(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        yield a  # 把a的值返回给num
        # 如果一个函数中有yield语句，那么这个就不是函数，而是一个生成器模板
        a, b = b, a+b
        current_num += 1


# 这个时候调用函数，创建的是一个生成器对象
obj = fibo_num(10)
print(obj)
for num in obj:
    print(num)

# it = iter()用于创建迭代器对象，next（it）用于输出迭代器的下一个元素
