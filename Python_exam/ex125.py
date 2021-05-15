phone_number = {'011': 'SKT', '016': 'KT', '019': 'LGU', '010': '알수없음'}

test = input('휴대전화 번호 입력: ')

a = test.split('-')[0]

print('당신은 %s 사용자입니다.' % phone_number[a])