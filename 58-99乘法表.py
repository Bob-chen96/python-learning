i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("*", end=' ')  # 实现不换行
        j += 1
    print() # 默认换行

    i += 1
print("----------")

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d * %d = %d" % (i, j, i*j), end=' ')  # 实现不换行
#         j += 1
#     print()  # 默认换行
#
#     i += 1

# for 循环打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d" % (j, i, j*i), end=" ")

    print()
