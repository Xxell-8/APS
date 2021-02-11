import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))[::-1]

    sell_point = prices[0]
    total = 0

    for idx in range(1, n):
        if sell_point > prices[idx]:
            total += sell_point - prices[idx]
        else:
            sell_point = prices[idx]

    print('#{} {}'.format(tc, total))