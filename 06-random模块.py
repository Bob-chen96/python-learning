import random  # 导入模块

computer = random.randint(1,3)  # 随机一个1-3的整数，闭区间

user = int(input("请输入你的拳法：1.石头 2.剪刀 3.布:"))  # 这里要转换成整数

print("computer:",computer)

print("user:", user)

if computer == 1:
    if user == 1:
        print("平局")
    elif user == 2:
        print("电脑获胜")
    else:
        print("用户获胜")

elif computer == 2:
    if user == 1:
        print("用户获胜")
    elif user == 2:
        print("平局")
    else:
        print("电脑获胜")
else:
    if user ==1:
        print("电脑获胜")
    elif user == 2:
        print("用户获胜")
    else:
        print("平局")


