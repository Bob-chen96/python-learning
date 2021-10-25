# 匿名函数：省略了def定义函数的标志步骤，可以定义功能简单的函数
# 语法： lambda 参数：表达式
# 特点：匿名函数把表达式作为整个返回值进行返回
func = lambda x:x+100  # 参数时x
print(func) # fanc保存的是匿名函数的地址
print(func(50))

print(lambda x, y: x + y(100, 200))

# 匿名函数可以作为函数的参数

f = lambda x,y: x*y
print(f(1,2))
