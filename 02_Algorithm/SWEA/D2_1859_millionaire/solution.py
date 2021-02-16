import sys
sys.stdin = open('input.txt')

## KEY > 역순으로 탐색 ##

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 1. 역순으로 탐색하기 위해 리스트 뒤집기
    prices = list(map(int, input().split()))[::-1]

    # 2. 판매 가격을 잡고
    sell_point = prices[0]
    total = 0

    for idx in range(1, n):
        # 3. 판매 가격보다 저렴하면 total에 차액 더하기
        if sell_point > prices[idx]:
            total += sell_point - prices[idx]
        # 4. 판매 가격보다 (같거나) 비싸면 판매가를 바꾸기
        else:
            sell_point = prices[idx]

    print('#{} {}'.format(tc, total))