import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    min_value = a + b - n
    if a >= b:
        max_value = b
    else:
        max_value = a

    print('#{} {} {}'.format(tc, max_value, min_value))