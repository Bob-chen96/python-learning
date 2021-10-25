"""匹配开头结尾
字符  功能
^  匹配字符串开头
$  匹配字符串结尾
"""

import re

names = ["name1", "_name", "2_name", "__name__"]

for name in names:
    ret = re.match(r"^[-zA-Z_][a-zA-Z0-9_]*$", name)
    if ret:
        print("变量名：%s 符合要求,匹配的数据是：%s", (name, ret.group())) # 相当于name
    else:
        print("变量名：%s 不符合要求...." % name)

