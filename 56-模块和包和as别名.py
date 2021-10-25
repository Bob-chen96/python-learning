# 一个py文件就是一个模块
import hm_model_test as Hm1  # as可以给模块起别名，要符合大驼峰命名

# 模块名.变量名
print(Hm1.name)

# 模块名.函数名()
Hm1.exam()

# 模块名.类名（） 创建对象
Tom = Hm1.Cat()
Tom.eat()

# import 模块名 是一次性把模块中所有工具全部导入，并且通过别名/模块名访问