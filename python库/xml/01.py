import xml.etree.ElementTree as ET
from lxml import etree

# ElementTree类：这个一个主要的类，大部分函数都通过它来进行。使用Element工厂函数很容易建立起一个xml元素。
# 访问标签名，用tag属性
# root = etree.Element("root")
# print(root.tag)  # root
#
# # 添加子节点方法1，append（）方法
# root.append(etree.Element('child1'))
# # 更有效的方法是SubElement工厂函数
# child2 = etree.SubElement(root, 'child2')
# child3 = etree.SubElement(root, 'child3')
# # 使用tostring 方法，可以看到刚才建立的 xml文件全貌。
# print(etree.tostring(root, pretty_print=True))
# print(root.iterchildren)

# 打开文件，读取xml文件对象
# tree = ET.parse('test_add_bookmark.xml')
# print(tree)

root = etree.parse('test_add_bookmark.xml').getroot()
# print(root)
# print(root.iterchildren())
# print(root.tag)
# print(root.attrib)
for child in root:
    print(child)
    print(child.tag)
    # print(child.attrib)
for c in child:
    print(c)
    # print(c.tag)
    print(c.attrib)
# for testcase in root.iterchildren():
#     print(testcase)