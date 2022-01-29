import jpype

# getDefaultJVMPath 获取默认的 JVM 路径
jvm_path = jpype.getDefaultJVMPath()
jpype.startJVM(jvm_path, '-ea', convertStrings=False)
# 利用jpype调用输出语句
jpype.java.lang.System.out.println('Success')
# shutdownJVM()关闭JAVA虚拟机
jpype.shutdownJVM()


