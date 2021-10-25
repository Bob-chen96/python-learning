# readline方法一次读取一行内容，把指针移到下一行开始位置

file = open("info.txt", "r", encoding="utf-8")

# 死循环读取全部数据
while True:
    line_text = file.readline()
    print(line_text,end="")

    if len(line_text) == 0:
        break

# 读取所有内容，返回列表
lines = file.readlines()
print(lines)

file.close()