finish_code = 90

print("完成率:%d%%" %finish_code)
# %d表示格式化整形变量，%%表示一个%

print("------------------------")

name = "小明"
age = 20
height = 170.5

print("姓名：%s 年龄：%d 身高:%.1f" % (name, age, height))
#  多个变量格式化输出

print("-----------------------------")
print("姓名：%s 年龄：%s 身高:%s " % (name, age, height))
# 任意数据类型都可以转换为字符串，所有占位符都可以换为%s