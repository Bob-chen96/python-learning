"""
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。
要求：
1. 校验输入内容是否符合规范（xx@polo.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾
2. 可以循环“输入--输出判断结果”这整个过程
3. 按字母 Q（不区分大小写）退出循环，结束程序
"""
import re

while True:
    email = input("请输入您的邮箱:")
    ret = re.match(r"^[a-z]+@[a-z]+\.com$", email)
    if email.upper() == 'Q':
        break
    else:
        if ret:
            l = email.split('@')
            print(f"{l[0]} {l[1]}")
        else:
            raise ValueError("incorrect email format")
