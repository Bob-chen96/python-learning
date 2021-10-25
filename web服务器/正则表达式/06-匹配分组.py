"""
字符  功能
|    匹配左右任意一个表达式
（ab） 将括号中字符作为一个分组
\num   引用分组num匹配到的字符串
（?P<name>） 分组起别名
（?P=name）  引用别名为name分组匹配到的字符串
"""

import re


def main():
    ret = input("请输入您的邮箱地址：")

    # 正则表达式中若要某些特殊字符，如.?等，需要在前面加上\进行转义
    # 用（）进行分组，可通过group（组数）返回每个组的匹配数据
    # |表示或，满足一个就可匹配
    num = re.match(r"([a-zA-Z0-9_]{4,20})@(163|qq)\.com$", ret)

    # r"(w*)[a-z]\1" \1表示取和第一个分组的数据一样

    if num:
        print("您输入的邮箱:%s 符合要求" % ret)
        print("第一组的数据是:%s" % num.group(1))
    else:
        print("您输入的邮箱:%s 不符合要求，请重新输入" % ret)


main()

html_str = "<body><h1>hahahhah</h1></body>"

ret = re.match(r"<(?P<p1>\w*)><(?P<p2>)\w*>.*</(?P=p2)></(?P=p1)>", html_str)
print(ret.group())