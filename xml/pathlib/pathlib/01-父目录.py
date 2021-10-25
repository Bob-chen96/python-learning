from pathlib import Path
import shutil
# 获取当前目录 D:\pycharm\py_project\pytest-练习\Python开发学习\python库\pathlib
current_path = Path.cwd()
print(current_path)

shutil.copytree(current_path.parent, current_path.parent.parent.joinpath('xml\\pathlib'))

# 获取home目录 C:\Users\86189
home_path = Path.home()
print(home_path)

# 获取上级目录
print(current_path.parent)

# 获取上上级父目录
print(current_path.parent.parent)

# parents属性就可以遍历整个父目录
for p in current_path.parents:
    print(p)
print(type(current_path.parents))

