# 文件操作步骤
"""1.打开文件
    2.读写文件：读将文件内容读入内存，写将文件内容写入文件
    3.关闭文件
"""
# 1.打开文件
# 要指定文件编码模式，windows默认是gbk
file = open("readme.txt",encoding="utf-8")
# 2.操作文件
# read方法一次性读取文件全部内容，下次再读取时，将读不到任何内容
# read读取文件内容的数据类型是字符串
text = file.read()
print(text)
print(type(text))

# 3.关闭文件
# 不关闭文件会造成系统资源的浪费
file.close()



