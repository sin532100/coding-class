a = input('우편번호: ')
b = a[:3]

c = ['010', '011', '012']
d = ["014", "015", "016"]

if b in c:
    print('강북구')
elif b in d:
    print('도봉구')
else:
    print('노원구')