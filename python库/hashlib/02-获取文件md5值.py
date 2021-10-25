import hashlib


def get_md5(file_name):
    file_txt = open(file_name, "rb").read()
    # 调用一个md5对象
    m = hashlib.md5(file_txt)
    # hexdigest()方法来获取摘要（加密结果）
    value = m.hexdigest()
    print(value)
    return value


get_md5(r"D:\1\8.ofd")
get_md5(r"D:\1\8-1.ofd")
