str = "Hello,python,python!"

print(str.replace('python', 'java')) # 默认全部替换

print(str.upper()) # 返回大写后的str

print(str.split(',')) # 按，进行切割返回列表

print(str.split(',',1)) # 切割一次

print(str)
# 这里str不会变，字符串不能被修改

print('#'.join(str))
# 以#为分隔符，将str中所有元素合并成一个新的字符串

print(str[0:5:1])  # 切片，左闭右开
print(str[6::2]) # 从6切到结尾

print(str[-1:-8:-1]) # 逆序
print(str[:13:-1])
print(str[::-1]) # 字符串全部倒序