# 当前py文件自己运行，__name__中是字符串
print(__name__)  # 输出__main__字符串

# 当前文件被别人导入，__name__是字符串 模块名

# 所用场景：
# if __name == "__main__" ：   表示被导入时不会执行该函数
#     函数()
