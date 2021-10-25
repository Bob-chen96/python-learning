def sum_1():
    '''
    当前函数实现两个数相加
    :return:
    '''
    num1 = 10  # 定义变量
    num2 = 20
    ret = num1+ num2
    print("%d + %d = %d" %(num1, num2, ret))
    print(f"{num1} + {num2} = {ret}") # 两个实现一样

sum_1()

def sum_2(num1, num2):
    ret = num1+ num2
    print("%d + %d = %d" % (num1, num2, ret))
sum_2(1,1)

#  num1叫形参，1叫实参