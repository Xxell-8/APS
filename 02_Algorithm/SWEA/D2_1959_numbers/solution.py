import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        a, b = b, a

    result = 0
    for case in range(m-n+1):
        total = 0
        for i in range(n):
            total += a[i] * b[i+case]
        if total > result:
            result = total

    print('#{} {}'.format(tc, result))