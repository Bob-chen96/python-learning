import copy

# 赋值表示将a指向存储11的位置，而不是在a中存储11，属于浅拷贝
a = [11, 22]

# 深拷贝，将11存储到b中
b = copy.deepcopy(a)

# 浅拷贝
c = copy.copy(a)

print(id(b))
print(id(c))

a.append(33)
print(b)
print(c)


