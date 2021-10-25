'''
1.模块就好比工具包，使用这个工具包的工具，需要导入这个模块
2.每一个py文件都是一个模块，如random.py
3.在模块中定义的全局变量，函数都是模块能够提供给外界直接使用的工具
'''
# 先在文件夹创建一个model_test.py文件
import hm_model_test   # 导入工具包

# 使用工具包中的工具
print(hm_model_test.name)  # 模块名.变量名
hm_model_test.exam()    # 模块名.函数名（参数）