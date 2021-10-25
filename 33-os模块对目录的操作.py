import os

# 1. os.listdir(目录名) 查看指定目录下所有文件，以列表形式展示，默认获取当前目录
print(os.listdir(r"D:\test_file_save"))  # .表示当前文件目录
os.remove(r'D:\test_file_save\1.ofd')

# 2. os.mkdir(目录名) 创建目录
# os.mkdir(r"C:\Users\Bob Chen\Desktop\1")
# os.mkdir("1")

# 3.os.rmdir（目录名） 删除目录,只能删除空目录
os.rmdir("1")
# shutil.rmtree(目录名) 可以删除非空目录，要导入shutil模块

# 4. os.getcwd()获取当前目录
print(os.getcwd())

# 5.os.chdir(目标目录)  修改工作目录，和切换目录相似
os.chdir("1")
print(os.getcwd())

# 6.os.path.isdir(文件夹路径)  判断是否是文件夹
print(os.path.isdir("."))

# 7. os.path.exists(目录/文件)  判断指定目录或文件是否存在
print(os.path.exists("1.txt"))

# 获取环境变量地址
print(os.getenv('JAVA_HOME'))
#  D:\\JAVA\\jdk-15.0.1

