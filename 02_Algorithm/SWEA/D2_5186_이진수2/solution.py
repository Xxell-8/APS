import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    num = float(input())
    result = ''

    for i in range(13):
        num *= 2
        result += str(int(num) % 2)
        if not num % 1:
            break
    else:
        result = 'overflow'

    print('#{} {}'.format(tc, result))