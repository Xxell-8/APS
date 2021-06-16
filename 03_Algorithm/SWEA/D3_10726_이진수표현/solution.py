# KEY > 2진수는 10진수를 2로 나눈 나머지를 모아 거꾸로 붙이면 완성

import sys
sys.stdin = open('input.txt')


# 2. 마지막 n개 자리를 체크하는 함수 생성
def check(n, m):
    # 2-1. n번 반복 동안
    for _ in range(n):
        # 2-2. 나머지가 없으면 0이므로 False
        if not m % 2:
            return False
        m //= 2
    return True



T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, m = map(int, input().split())
    result = 'ON' if check(n, m) else 'OFF'

    print('#{} {}'.format(tc, result))