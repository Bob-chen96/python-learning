# 打开源文件
file1 = open("info.txt", "r", encoding="utf-8")
# 打开目标文件
file2 = open("new2.txt", "w", encoding="utf-8")

# 使用readline按行读取，读一行复制一行，配合while循环
while True:
    text = file1.readline()
    file2.write(text)

    if len(text) == 0:
        break

file1.close()
file2.close()