import re

# re.search 扫描整个字符串并返回第一个成功的匹配,不用从头开始匹配

ret = re.search(r"\d+", "22阅读数是5555")
print(ret)

# findall 提取所有匹配数据生成列表
ret = re.findall(r"\d+", "22阅读数是5555")
print(ret)

# sub将匹配到的数据进行替换

ret = re.sub(r"\d+", "998", "python = 5")
print(ret)

# split根据匹配进行切割字符串，并返回一个列表
ret = re.split(r":", "身高:172, 体重:65")
print(ret)
