# open函数默认以只读方式打开文件
"""
访问方式：
r：只读方式，文件不存在，会报错
w：只写方式，文件存在，进行内容覆盖，写入字符串，不存在，新建
a：追加方式，文件存在，在文件末尾追加，不存在新建文件
r+，w+，a+：读写方式打开文件
"""
# f = open(r"绝对路径/1.txt", "w", encoding="utf-8") 打开其他路径文件
f = open("readme.txt", "w", encoding="utf-8") # 以只写方式打开

text = f.write("写入文件") # 覆盖并写入数据,只能写入字符串
print(text)  # 把原文件覆盖，返回字符串长度


f.close()

f2 = open("readme.txt", "a",encoding="utf-8")
add_text = f2.write("追加数据")
print(add_text)

f2.close()