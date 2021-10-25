class Stack:
    def __init__(self):
        self.__list = []

    # 入栈
    def push(self, item):
        self.__list.append(item)

    # 出栈
    def pop(self):
        return self.__list.pop()

    # 返回栈顶元素
    def speek(self):
        return self.__list[-1]

    def is_empty(self):  # 判断是否已为空
        return not self.__list

    def size(self):  # 返回栈中元素个数
        return len(self.__list)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push('a')
    s.push(True)
    print(s)