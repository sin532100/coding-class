data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

b = []

for i in data:
    for a in i:
        print(a*1.00014)
        b.append(a*1.00014)
    print('----')

print(b)