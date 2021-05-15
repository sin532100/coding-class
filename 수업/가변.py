
def add(a, b, *c):
    d = a + b
    for i in c:
        d += i 
    return d

e = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(e)

print('a', 'abc', sep=' : ')