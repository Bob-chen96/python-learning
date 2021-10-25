with open(r'C:\Users\86189\Desktop\1.ini','r',encoding='gbk') as f:
    contents = f.readlines()

with open(r'C:\Users\86189\Desktop\1.ini','w',encoding='gbk') as n_f:
    for content in contents:
        if "125%" in content:
            content = content.replace('125%', '150%')
        n_f.write(content)


