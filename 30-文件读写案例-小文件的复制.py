# 把小源文件内容拷贝到目标文件中

# 打开源文件
file1 = open("info.txt", "r", encoding="utf-8")
# 打开目标文件
file2 = open("new.txt", "w", encoding="utf-8")

# 读取源文件内容
text = file1.read()
file2.write(text)

# 关闭文件
file1.close()
file2.close()

