import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    q = a // b
    r = a % b

    print('#{} {} {}'.format(tc, q, r))