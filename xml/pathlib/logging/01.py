import logging

"""
用作记录日志，默认分为六种日志级别（括号为级别对应的数值）
NOTSET（0）
DEBUG（10）
INFO（20）
WARNING（30）
ERROR（40）
CRITICAL（50）

special
在自定义日志级别时注意不要和默认的日志级别数值相同
logging 执行时输出大于等于设置的日志级别的日志信息，如设置日志级别是 INFO，则 INFO、WARNING、ERROR、CRITICAL 级别的日志都会输出。
"""

"""
logging 使用非常简单，使用  basicConfig()  方法就能满足基本的使用需要；如果方法没有传入参数，会根据默认的配置创建Logger 对象，默认的日志级别被设置为 WARNING
filename: 日志输出到文件的文件名
filemode: 文件模式，r[+]、w[+]、a[+]
format: 日志输出的格式
datefat: 日志附带日期时间的格式
style: 格式占位符，默认为 "%" 和 “{}”
level: 设置日志输出级别
stream: 定义输出流，用来初始化 StreamHandler 对象，不能 filename 参数一起使用，否则会ValueError 异常
handles: 定义处理器，用来创建 Handler 对象，不能和 filename 、stream 参数一起使用，否则也会抛出 ValueError 异常
"""
logging.basicConfig(level='DEBUG', filename='01.log', filemode='a')

logging.debug('崔庆才丨静觅、韦世东丨奎因')
logging.warning('邀请你关注微信公众号【进击的 Coder】')
logging.info('和大佬一起coding、共同进步')