import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    d, l, n = map(int, input().split())

    damage = 0
    for i in range(n):
        damage += d*(1 + i * (l/100))

    print('#{} {}'.format(tc, int(damage)))