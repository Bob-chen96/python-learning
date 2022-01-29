file = r"C:\Users\86189\Desktop\电子公文交换系统-用例 - 副本.csv"

with open(file, 'r') as f:
    contents = f.readlines()
    print(contents)

with open(file, 'w', encoding='gbk') as w:
    for content in contents:
        if '公文管理"' in content:
            content.replace("公文管理", "其他管理")

