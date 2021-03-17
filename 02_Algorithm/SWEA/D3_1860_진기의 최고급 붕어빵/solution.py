import sys
sys.stdin = open('input.txt')


def reservation(n, m, k, order):
    # 2. 손님 도착 시간 순으로 정렬
    order.sort()
    # 3-1. order를 받으면서
    for idx in range(n):
        # 3-2. 현재까지 만든 붕어빵 food 계산
        food = (order[idx] // m) * k
        # 3-3. 이전까지 팔린 붕어빵 sold 계산
        sold = idx
        # 3-4. 현재 손님이 살 수 있는 붕어빵이 없으면 impossible
        if food - (sold+1) < 0:
            return 'Impossible'
    # 3-5. 끝까지 order를 다 받으면 possible
    return 'Possible'

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, m, k = map(int, input().split())
    order = list(map(int, input().split()))

    print('#{} {}'.format(tc, reservation(n, m, k, order)))