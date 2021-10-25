from pathlib import Path

example_path = Path(r'D:\pycharm\py_project\pytest\Python开发学习\python库\abc.py')
print(example_path)
print(type(example_path))
# D:\pycharm\py_project\pytest-练习\Python开发学习\python库\abc.py

"""name返回目录的最后一个部分"""
print(example_path.name)
# abc.py

"""suffix 目录中最后一个部分的扩展名"""
print(example_path.suffix)
# .py

"""suffixes 返回多个扩展名列表"""

"""stem 目录最后一个部分，没有后缀"""
print(example_path.stem)
# abc

"""with_name(name) 替换目录最后一个部分并返回一个新的路径"""
print(example_path.with_name('gbk.zip'))
# D:\pycharm\py_project\pytest-练习\Python开发学习\python库\gbk.zip

"""with_suffix(suffix) 替换扩展名，返回新的路径，扩展名存在则不变"""
print(example_path.with_suffix('.doc'))
# D:\pycharm\py_project\pytest-练习\Python开发学习\python库\abc.doc

