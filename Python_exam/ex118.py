warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

test = input('종목 선택: ')

if test in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')