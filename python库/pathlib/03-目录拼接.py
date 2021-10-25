from pathlib import Path
import logging

"""直接传进一个完整字符串"""
example_path1 = Path("/Users/Anders/Documents/powershell-2.jpg")
print(example_path1)
# \Users\Anders\Documents\powershell-2.jpg

"""也可以传进多个字符串"""
example_path2 = Path(
    "\\", "Users", "dongh", "Documents", "python_learn", "pathlib_", "file1.txt"
)
print(example_path2)
# \Users\dongh\Documents\python_learn\pathlib_\file1.txt

"""也可以利用Path.joinpath()"""
new_path = example_path1.joinpath("1.txt")
print(new_path)
# \Users\Anders\Documents\powershell-2.jpg\1.txt

"""利用 / 可以创建子路径"""
example_path3 = example_path1 / "2.doc"
print(example_path3)
# \Users\Anders\Documents\powershell-2.jpg\2.doc

