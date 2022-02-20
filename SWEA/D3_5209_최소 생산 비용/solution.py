import sys
sys.stdin = open('input.txt')


def pick_factory(pdx, total):
    global result, selected

    # 2-1. 계산 중인 total이 최솟값이 될 수 없으면 return
    if total >= result:
        return

    # 2-2. 최솟값으로 n개 다 계산하면 result 갱신 후 return
    if pdx == n:
        result = total
        return

    for fdx in range(n):
        # 3-1. 해당 공장이 선택된 적 없으면,
        if not selected[fdx]:
            # 3-2. 선택하고 다음 상품으로 넘어가기
            selected[fdx] = 1
            pick_factory(pdx + 1, total + prices[pdx][fdx])
            # 3-3. 원상복구
            selected[fdx] = 0


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받고
    n = int(input())
    prices = [list(map(int, input().split())) for _ in range(n)]
    # 1-2. 필요한 변수 초기화
    selected = [0] * n
    result = 100 * n

    pick_factory(0, 0)
    print('#{} {}'.format(tc, result))