"""
如果有一个列表a=[1,3,5,7,11]
问题：1如何让它反转成[11,7,5,3,1]
2.取到奇数位值的数字，如[1,5,11]
"""

a = [1, 3, 5, 7, 8, 11]
a.sort(reverse=True)
print(a)

for i in a:
    if i % 2 == 0:
        a.remove(i)
    print(a)
print(a)


