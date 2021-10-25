"""
有一个数据list of dict如下
a = [
    {"test1": "123456"},
    {"test2": "123456"},
    {"test3": "123456"},
]
写入到本地一个txt文件，内容格式如下：
test1,123456

test2,123456

test3,123456
"""

list = [
    {"test1": "123456"},
    {"test2": "123456"},
    {"test3": "123456"},
]
with open('1.txt', mode='w') as f:
    for data in list:
        for key,value in data.items():
            f.write(f"{key},{value}\n")

