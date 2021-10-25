my_dict = {'name':'张三','age':22,'gender':'女'}
print(type(my_dict))

print(my_dict['name'])

print(my_dict.get('name'))

print(my_dict.get(1)) # 返回None

my_dict['age'] = 25
print(my_dict) # 修改key对应的value值

my_dict['addr'] = '湖北武汉'
print(my_dict) # 新增键值对

my_dict.setdefault('name','Bob')
print(my_dict)  # 这里不会改变name对应的value值

my_dict.update({'name':'Bob','weight':60})
print(my_dict)  # 更新name对应的value,新增weight

del my_dict['weight']
print(my_dict)   # 删除键值对
