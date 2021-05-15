import random


def print_up_down(dap, moon):
    if dap == moon:
        print('정답입니다!!', moon)
    elif dap > moon:
        print('입력한 값이 작습니다.')
    elif dap < moon:
        print('입력한 값이 큽니다.')

dap = random.randint(1, 1000)

while True:
    print_up_down(dap, int(input('숫자를 입력하세요: ')))
