# def fun(a, b=[]):
#     b += [a]
#     print(b)
#
# fun(1)
# fun(2, [])
# fun(3)

def fun(A):
    if len(A)==1:
        return A[0]
    else:
        A1 = A[0:len(A)-2]
        A2 = A[1:len(A)-1]
        A3 = A[2:len(A)]
        return fun(A1) * fun(A2) * fun(A3)


print(fun([1, 2, 3]))
print(fun([2,4,5]))
