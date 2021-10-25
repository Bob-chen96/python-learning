# 遍历列表
list_1 = [100, 'python', True, 10.0, (1, 2)]
for value in list_1:
    print(value)

# 遍历元组
tuple_1 = (10, 20, 30, [1, 'py'])
for i in tuple_1:
    print(i)

# 遍历字符串
str_1 = "hello world !"
for i in str_1:
    print(i)

# 遍历字典
my_dict = {'name':'张三','age':22,'gender':'女'}
for k in my_dict:
    print(k)  # 这里是遍历打印键（key）值
    print(k, my_dict[k])

