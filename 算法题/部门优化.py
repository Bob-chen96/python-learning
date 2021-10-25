# 创建一个字典存放4个ABCD组人员
s = {"A": 10, "B": 7, "C": 5, "D": 4}
for i in range(10):
    # 将字典中value值最大的键赋值给max_key
    max_key = max(s, key=lambda k: s[k])
    for k in s:
        # 如果字典中key值对应max_key，则对应的value值减三，反之，value值+1
        if k == max_key:
            s[max_key] -= 3
        else:
            s[k] += 1

print(s)

