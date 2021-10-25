import shutil

# 把src文件复制到dst目录下，两个参数为文件名称，若dst存在则进行覆盖
shutil.copyfile(src='1.txt', dst='2.txt')

# 移动文件，目录或者文件，目录重命名,若dst存在则不可覆盖
shutil.move(src, dst)

# 复制一个文件到一个文件或一个目录 ，注意：src必须为文件，dst为文件或目录
shutil.copy(src, dst)

