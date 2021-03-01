import sys
sys.stdin = open('input.txt')


def solution(n, m, k, order):
    order.sort()
    for idx in range(n):
        food = (order[idx] // m) * k
        sold = idx
        if food - (sold+1) < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    order = list(map(int, input().split()))

    print('#{} {}'.format(tc, solution(n, m, k, order)))