import sys
sys.stdin = open('input.txt')


def harvest(n, farm):
    # 1-1. 수확한 농작물 합계 total
    total = 0
    # 1-2. 수확하지 않을 부분 rotten
    rotten = n // 2
    # 1-3. 수확 범위 fresh
    fresh = 1

    row = 0
    while row < len(farm):
        for i in range(fresh):
            total += int(farm[row][rotten + i])

        if row < n // 2:
            rotten -= 1
            fresh += 2
        else:
            rotten += 1
            fresh -= 2

        row += 1

    return total

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    farm = [input() for _ in range(n)]
    print('#{} {}'.format(tc, harvest(n, farm)))