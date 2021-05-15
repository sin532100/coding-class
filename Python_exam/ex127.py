a = input('주민등록번호: ')

b = a.split('-')[1]

if b[0] in ['1','3']:
    print('남자')
else:
    print('여자')