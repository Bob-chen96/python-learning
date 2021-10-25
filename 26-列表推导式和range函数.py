# range 语法
# 作用：产生序列数对象（容器），可以使用for循环遍历
# 说明：range(起始位置，结束位置，步长) 步长默认为1可以省略，步长可以为负
# range生成的范围包含起始位置值，不包含结束位置值

print(range(0, 10, 1))
print(type(range(0, 10, 1)))  # range类型

for i in range(0, 10, 1):
    print(i)  # 打印0-9

# 列表推导式
# 作用： 快速创建简单列表
print([x for x in range(5)])   # 打印列表[0, 1, 2, 3, 4]

d = [z + 100 for z in range(5)]
print(d)

g = [i for i in range(21) if i%2 == 0]
print(g)  # 可添加if条件判断