# import 模块名 是一次性把模块中所有工具全部导入，并且通过别名/模块名访问
# from 模块 import 工具 导入一个工具
# 导入后，不需要通过模块名，可直接使用工具--全局变量，函数，类

from hm_model_test import name  # 导入全局变量
from hm_model_test import age as age1  #  当多个模块有相同工具名时，可以用as
from hm_model_test import exam  # 导入函数
from hm_model_test import Cat   # 导入类
# from hm_model_test import *  导入所有工具，但是多个模块容易出现同名工具
print(name)

print(age1)
exam()

Tom = Cat()
Tom.eat()

# 导入模块时，先在当前目录下查找，找到了就导入，没找到就导入系统模块
# 模块名.__file__ 查看模块路径
import random
print(random.__file__)

