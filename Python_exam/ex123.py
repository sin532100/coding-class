dic = {'달러': 1167, '엔': 1.096, '유로': 1268, '위안': 171}

test = input('입력: ')

split2 = test.split()

print(float(split2[0]) * dic[split2[1]], '원')