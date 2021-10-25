"""
包是一个包含多个模块的特殊目录
目录下有一个特殊的文件__init__.py
包名的命名方式和变量一样  小写字母+_
"""
# 使用 import 包名 可以一次性导入包中所有模块

# 1. import 包名  包名.模块名.函数名()  进行导入
import package_example
# 2.from 包名 import 模块名  模块名.函数名（） 进行导入
from package_example import send_message
from package_example import receive_message
# from . import 模块名  表示从当前目录导入模块

package_example.send_message.send()

receive_message.receive()
