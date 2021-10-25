def merge(A, B):
    """这里规定A,B是两个有序数组
    定义i，j分别指向A和B的数组位置
    循环比较A[i], B[j]位置上的值,小的则提取值放在结果数据, 同时对应的指针+1
    另一个的指针不变.
    """
    # 定义一个数组保存返回的结果
    result = []
    # 初始指向位置0处
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    result += A[i:]
    result += B[j:]
    return result


A = [1, 4, 9]
B = [2, 3, 10]
print(merge(A, B))




