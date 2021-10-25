from pathlib import Path


def get_file():
    file_path = Path(__file__).parent.joinpath(r'1.txt')
    with open(file_path, 'r',encoding='utf-8') as f:
        value = [(i.strip()) for i in f.readlines()]
    print(value)
    return value


get_file()