import httpx

# 获取一个网页
r = httpx.get('https://httpbin.org/get')
print(r)
print(type(r))
# <Response [200 OK]>
# <class 'httpx.Response'>


"""PUT，DELETE，HEAD和OPTIONS请求都遵循相同的样式："""
r = httpx.put('https://httpbin.org/put', data={'key': 'value'})
print(r)
r = httpx.delete('https://httpbin.org/delete')
r = httpx.head('https://httpbin.org/get')
r = httpx.options('https://httpbin.org/get')


"""在url中传递参数"""
# 要在请求中包括URL查询参数，可以使用params关键字
params = {'key1': 'value1', 'key2': 'value2'}
u = httpx.get("https://httpbin.org/get", params=params)
print(u.url)  # https://httpbin.org/get?key1=value1&key2=value2

"""响应内容"""
# HTTPX将自动处理将响应内容解码为Unicode文本
t = httpx.get("https://www.example.org/")
print(t.text)
# 检查已使用哪种编码来解码响应
print(t.encoding)  # UTF-8

print(t.json())


