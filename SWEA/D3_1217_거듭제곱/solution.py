import sys
sys.stdin = open('input.txt')

# KEY > 분할 정복 적용

def involution(base, exponent):
    # 1. return 조건 생성
    if base < 2 or exponent == 1:
        return base
    elif exponent == 0:
        return 1

    # 2-1. 지수가 홀수면, 짝수로 만들고 재귀
    if exponent % 2:
        new_base = involution(base, (exponent-1) // 2)
        return new_base ** 2 * base
    # 2-2. 지수가 짝수면, 바로 재귀
    else:
        new_base = involution(base, exponent // 2)
        return new_base ** 2


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    base, exponent = map(int, input().split())

    print('#{} {}'.format(tc, involution(base, exponent)))