"""
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）
"""

import math

num = []
for i in range(100, 1000):

    m = str(i)
    a, b, c = int(m[0]), int(m[1]), int(m[2])
    if int(m) == math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3):
        num.append(m)
        print(num)
print(num)
