import os
import shutil
# 1.批量创建文件
def create_files():
    # 判断目录是否存在
    if os.path.exists(r".\files"):
        shutil.rmtree(r".\files")  # 删除文件夹
    # 先创建目录
    os.mkdir(r".\files")
    # 切换到工作目录
    os.chdir(r".\files")
    # 在该文件夹下批量创建文件
    print(os.getcwd())
    for i in range(1, 21):
        # file = open("new" + str(i) + ".txt", "w", encoding="utf-8")
        file = open("new%d.txt" %i, "w", encoding="utf-8")  # 两个效果一样
        file.write("1111")
        file.close()

# 2.批量修改文件名
def change_files_name():
    # 查看当前目录是否是files目录，不是要切换到目录下
    if os.getcwd() != r"D:\pycharm\py_project\pytest\Python基础\案例-批量修改文件名\files":
        os.chdir(r"D:\pycharm\py_project\pytest\Python基础\案例-批量修改文件名\files")
    # 如果在，获取当前目录所有内容
    file_name = os.listdir()
    print(file_name)
    # 循环遍历列表，修改文件名
    for name in file_name:
        os.rename(name, "new_"+name)
    print(file_name)


# 调用函数
create_files()
change_files_name()