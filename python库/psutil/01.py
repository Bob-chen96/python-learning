"""
    psutil模块可以跨平台使用，支持Linux，Windows等，它
主要用来系统监控，性能分析，进程管理等。

"""

import psutil
# 获取CPU完整信息
print(psutil.cpu_times())

# 查看CPU逻辑个数，为False时查看CPU物理个数
print(psutil.cpu_count(logical=True))

# 获取系统CPU使用率，有两个参数interval和percpu
# interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率
print(psutil.cpu_percent())

# 获取系统内存的使用情况
print(psutil.virtual_memory())

# 获取系统交换内存的统计信息
print(psutil.swap_memory())

# 获取磁盘分区的信息
print(psutil.disk_partitions())

# 获取磁盘使用情况
print(psutil.disk_usage("/"))

# 获取磁盘的IO统计信息
print(psutil.disk_io_counters())

# 获取总的网络IO信息
print(psutil.net_io_counters())

# 获取网络接口信息
print(psutil.net_if_addrs())

# 获取网络接口状态信息
print(psutil.net_if_stats())

# 获取系统的开机时间
print(psutil.boot_time())

# 获取连接系统的用户列表
print(psutil.users())

# 获取系统全部的进程信息
print(psutil.pids())

# 获取单个进程信息
p = psutil.Process(9564)  # 获取指定进程ID=1988
print(p.name())  # 进程名
print(p.exe())  # 进程的bin路径
print(p.cwd())  # 进程的工作目录路径
print(p.cmdline())  # 进程启动的命令行
print(p.ppid())  # 父进程ID
print(p.parent())  # 父进程
print(p.children())  # 子进程列表
print(p.status())  # 进程状态
print(p.username())  # 进程的用户名
print(p.create_time())  # 进程创建的时间
print(p.cpu_times)  # 进程使用的CPU时间
print(p.memory_info())  # 进程使用的内存
print(p.num_threads())  # 进程的线程数量
print(p.threads())  # 所有线程信息

p.memory_full_info().uss

