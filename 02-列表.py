my_list = [100, 12.3, True, 'hello', 12.2]

print(type(my_list))
print(my_list[0])

my_list.insert(1, 200)  # 插入
print(my_list)

my_list.append('world')  # 在末尾添加数据
print(my_list)

my_list.append([300,400])
print(my_list)  # 插入列表

my_list.extend([500, 600])
print(my_list)

del my_list[0] # 删除索引为0的数据
print(my_list)

my_list.remove(600)
print(my_list)  # 删除指定数据

num = my_list.pop() # 返回的是删除的数据，默认删除末尾元素，可以添加索引
print(num)
print(my_list)

print(my_list[4])
print(my_list.index('world'))

print(len(my_list))
print(my_list.count(500))

my_list.clear()
print(my_list)  # 清空列表

list1 = [1, 20, 6, 59, 100, 7, 24]
list1.sort()
print(list1) # 升序排列

list1.sort(reverse=True)
print(list1)  # 降序排列

list1.reverse()
print(list1) # 列表数据反转


