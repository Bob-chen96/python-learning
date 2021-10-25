"""
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
如何得出c = ["a1", "b2", "c3", "d4", "e5"]
"""

a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
c = []
for m in b:
    n = b.index(m)
    i = a[n]
    c.append(f"{m}{i}")
    print(c)
print(c)

