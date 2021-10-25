"""
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都 等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据
"""

num = [1, 1]
for i in range(2, 101):
    m = num[i-2] + num[i-1]
    if m > 100:
        break
    num.append(m)
print(num)

