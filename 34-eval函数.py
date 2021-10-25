# eval（）函数十分强大，将字符串当成有效表达式来求值并返回计算结果
# 相当于去掉双引号
print(eval("3+5"))
print(type(eval("3+5"))) # 返回整数类型

print(eval("[1,200]"))
print(type(eval("[1, 200]")))  # 返回列表类型