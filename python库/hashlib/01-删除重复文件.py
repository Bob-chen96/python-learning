import hashlib
import os
import json


def get_md5(file_name):
    file_txt = open(file_name, "rb").read()
    # 调用一个md5对象
    m = hashlib.md5(file_txt)
    # hexdigest()方法来获取摘要（加密结果）
    value = m.hexdigest()
    return value


def delete_same_file(file_path):
    # try:
    #     with open('test.json', 'r', encoding='utf-8') as n_f:
    #         all_md5 = json.load(n_f)
    # except FileNotFoundError:
    all_md5 = {}
    delete_files = 0
    file_list = os.listdir(file_path)
    length = len(file_list)
    print(f"共有{length}个文件")
    for file in file_list:
        real_path = os.path.join(file_path, file)
        if os.path.isfile(real_path):
            new_md5 = get_md5(real_path)
            if new_md5 in all_md5.keys():
                os.remove(real_path)
                delete_files += 1
            else:
                all_md5[new_md5] = real_path
    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(all_md5, f)
    print(f"共删除{delete_files}个文件")



# get_md5(path + '\\' + '1.1_1字体_加粗.doc1570621187496.ofd')
# get_md5(path + '\\' + '1.1_1字体-字型.doc1570621187359.ofd')
# get_md5(path + '\\' + '1.txt')
# get_md5(path + '\\' + '2.txt')


if __name__ == "__main__":
    # test_path = r"D:\perform_test_data"
    test_path = r"D:\perform_test_data\1"
    delete_same_file(test_path)

