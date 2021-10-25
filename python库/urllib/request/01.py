import urllib.request

# 1.用urllib.request 里的urlopen()方法发送一个请求
# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen("https://www.baidu.com/")
# 服务器返回的类文件对象支持Python文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()
print(html)

# 2.用urllib.request 里的request ()方法发送一个请求
# url 作为Request()方法的参数，构造并返回一个Request对象
# Request实例，除了必须要有 url 参数之外，还可以设置另外两个参数：
# data：如果是GET请求，data（默认空），如果是POST请求，需要加上data参数，伴随 url 提交的数据。
# headers（默认空）：是一个字典，包含了需要发送的HTTP报头的键值对。
request = urllib.request.Request("https://www.baidu.com/")
# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
response = urllib.request.urlopen(request)
content = response.read()
print(content)







