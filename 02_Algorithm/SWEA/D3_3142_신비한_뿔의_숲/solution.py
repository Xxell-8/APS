import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    unicorn = m * 2 - n
    twinhorn = m - unicorn

    print('#{} {} {}'.format(tc, unicorn, twinhorn))