import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    result = 0

    count = 1
    while D >= 10 ** (-6):
        # A에서 B로 가는 경우
        if count % 2:
            t = D / (B + F)

        # B에서 A로 가는 경우
        else:
            t = D / (A + F)

        result += F * t
        D -= t * (A + B)
        count += 1

    print('#{} {}'.format(tc, result))