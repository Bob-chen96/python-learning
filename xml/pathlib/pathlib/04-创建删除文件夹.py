from pathlib import Path

"""
关于这里的创建文件目录mkdir方法接收两个参数：
parents：如果父目录不存在，是否创建父目录。
exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。
"""

path = Path(r'D:\pycharm\py_project\pytest\Python开发学习\python库\pathlib\test')

"""absolute() 也可以获取绝对路径，但是推荐resolve()"""
print(path.absolute())
path.mkdir()

path.rmdir()