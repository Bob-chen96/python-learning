import os
file_path = r"D:\perform_test_data"
file_list = os.listdir(file_path)
print(file_list)
print(len(file_list))
for file in file_list:
    if '1.11' in file:
        os.remove(file_path + '\\' + file)

