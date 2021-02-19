import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. 주어진 값을 받고
    n, a, b = map(int, input().split())

    # 2. 최솟값 구하기
    if a+b >= n:
        min_value = a + b - n
    else:
        min_value = 0

    # 3. 최댓값 구하기
    if a >= b:
        max_value = b
    else:
        max_value = a

    print('#{} {} {}'.format(tc, max_value, min_value))