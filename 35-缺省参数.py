#  定义函数时，具有默认值的参数就是缺省参数
def func(name, age=20, position = "学生"):
    print(name)
    print(age)
    print(position)
#  这里age和position都有默认值

func("张三")