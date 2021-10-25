# 1.无参数无返回值
def ex1():
    print("当前函数无参数无返回值")
ex1()

print('-'*30)
# 2.无参数有返回值
def ex2():
    print("当前函数无参数有返回值")
    tem = 27
    return tem
ret = ex2()
print(ret)

print('-'*30)

# 3 .有参数无返回值
def ex3(num):
    num += 100
    print(num)
    print("当前函数有参数无返回值")
ex3(100)

print('-'*30)

# 4.有参数有返回值
def login(user, pwd):
    """ 当前函数模拟登录操作"""
    my_user = 'Bob'  # 定义变量，模拟数据库中的账号密码
    my_pwd = 123456
    if user == my_user and pwd == my_pwd:
        return "登录成功，返回主页"
    else:
        return "账号或密码错误"

ret = login('Bob',123456)
print(ret)

