# 导入工具包
import os

# # 1. os.rename(源文件名，目标文件名)  重命名文件
# os.rename("readme.txt", "new_readme.txt")
#
# # 2. 删除文件 os.remove(文件名)
# os.remove(r"C:\Users\Bob Chen\Desktop\1.java")  # 支持相对和绝对路径

# 当前脚本的绝对路径
a = os.path.abspath(__file__)
print(a)
print(type(a))

# 返回path的父路径
print(os.path.dirname(a))
