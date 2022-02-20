import sys
sys.stdin = open('input.txt')

rules = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
         '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
         '0110111': 8, '0001011': 9}


def scan():
    code = []
    for i in range(8):
        num = rules[password[7*i:7*(i+1)]]
        code.append(num)
    return code


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    password = ''
    for _ in range(n):
        info = input().strip('0')
        if info:
            password = info
    password = password.zfill(56)

    code = scan()
    validation = 0
    for idx in range(7):
        if idx % 2:
            validation += code[idx]
        else:
            validation += code[idx] * 3
    validation += code[7]

    result = 0
    if not validation % 10:
        result = sum(code)

    print('#{} {}'.format(tc, result))