"""
正则表达式的单字符匹配：
.  匹配任意一个字符（除了\n）
[] 匹配[]中列举的字符
\d  匹配数字，即0-9
\D  匹配非数字
\s  匹配空白，即空格，tab键
\S 匹配非空白
\w 匹配单词字符，即a-z，A-Z,0-9,_
\W 匹配非单词字符

"""
import re

ret = re.match(r"hello", "hello9")
print(ret)  # 若匹配，就返回匹配对象，不匹配就返回None

print(ret.group())  # 返回匹配内容

ret = re.match(r"数据结构\d", "数据结构1")  # \d表示替换任意一个数字
print(ret)

ret = re.match(r"数据结构[1-8]", "数据结构1")  # [1-8]表示替换范围内的任何数值
print(ret)

ret = re.match(r"数据结构[1-8a-zA-Z]", "数据结构h")
print(ret)

ret = re.match(r"数据结构\w", "数据结构_")
print(ret)

ret = re.match(r"数据结构.", "数据结构!")  # .匹配任意一个字符
print(ret)