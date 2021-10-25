a = [1, 2, 3]
b = [1, 2]
print(id(a))
print(id(b))
print((a is b))
#  身份运算符is用来判断两个数据的引用地址是否相等，相等返回True
c = [1, 2]
print((c == b))  # == 用来判断两个数据值是否相等
