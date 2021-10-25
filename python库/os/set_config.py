# config_path = r'D:\local\git\suwell\config\const.py'
config_path = r'D:\work\autotest\suwell\config\const.py'


with open(config_path, 'r', encoding='utf-8') as f:
    contents = f.readlines()

with open(config_path, 'w', encoding='gbk') as w:
    for content in contents:
        if 'RUNNING_PROGRAM = "suwellreader"' in content:
            content = content.replace("RUNNING_PROGRAM = 'suwellreader'", "RUNNING_PROGRAM = 'wps'")
    w.write(content)

