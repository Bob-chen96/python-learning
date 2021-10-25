import collections
str = 'Hello python. Hello world'
# 将字符串按空格拆开，返回一个列表
list = str.split(' ')
# 通过counter函数用来记录值出现的次数
print(collections.Counter(list))