import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))[::-1]

    total = 0
    sell = prices.pop(0)
    buy = prices.pop(0)

    while True:
        while sell > buy:
            total += sell - buy
            if prices:
                buy = prices.pop(0)
            else:
                break

        if sell <= buy and prices:
            sell = buy
            buy = prices.pop(0)
        else:
            break

    print('#{} {}'.format(tc, total))