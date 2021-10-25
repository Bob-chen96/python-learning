'''
不可变数据类型：源内存中的数据不允许被修改
如果想要修改数据，需要开辟新的内存空间，让变量重新引用新内存地址

1.数字类型 int,bool,float,complex,long(2.x)
2.字符串 str
3.元组 tuple

可变数据类型：原内存空间数据可修改，不用开辟新的空间（重新赋值还是会改变地址）
1.列表 list
2.字典 dict
'''
# 浮点数
num1 = 13.3
print("num1: %s, id(num1)=%s" % (num1, id(num1)))

num1 += 3.6
print("num1: %s, id(num1)=%s" % (num1, id(num1)))  # 需用新的内存空间

# 列表
list1 = [10,20]
print(list1)
print(id(list1))

list1 += [30, 40]   # 直接在源内存地址中进行修改
print(list1)
print(id(list1))
