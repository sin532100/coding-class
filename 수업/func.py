
def addAll(a, b):
    c = 0
    for i in range(a, b+1):
        c += i
    return c

d = int(input())
e = int(input())

f = addAll(d, e)
print(f)

