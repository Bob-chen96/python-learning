import configparser

"""configParser解析的配置文件的格式比较象ini的配置文件格式，就是文件中由多个section构成，每个section下又有多个配置项"""

config_path = r"D:\1.ini"

# 创建管理对象
conf = configparser.RawConfigParser()

conf.read(config_path, encoding="utf-8")

# 获取所有section，返回list['General']
sections = conf.sections()
print(sections)

# 返回section的元素，以元祖形式
items = conf.items('General')
print(items)


# 删除一个 section中的一个 item（以键值KEY为标识
conf.remove_option('General', "test")

conf.set("General", 'display.zoom', '120%')
conf.set("General", 'annot.straightline.continue', '1')


# remove和set方法并没有真正的修改ini文件内容，只有当执行conf.write()方法的时候，才会修改ini文件内容
conf.write(open(config_path, "r+"))