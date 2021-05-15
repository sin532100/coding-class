test = int(input('입력값: '))

if test-20 < 0:
    print('출력값: 0')
elif test-20 <= 255:
    print('출력값:', test-20)
else:
    print('출력값: 255')