import os
from pathlib import Path
import shutil
import glob

save_dir = Path(r"D:\perform_test_data")

def save_filename_to_txt(file_path):
    p = Path(file_path)
    files = p.rglob("*.ofd")
    # print(len(list(files)))
    for file in files:
        print(str(file))
        # try:
        #     shutil.move(str(file), save_dir)
        # except:
        #     continue


if __name__ == '__main__':
    # save_filename_to_txt(r"D:\数科样例\数科测试样例")
    save_filename_to_txt(save_dir)