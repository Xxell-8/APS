import sys
sys.stdin = open('input.txt')


def harvest(n, farm):
    # 2-1. 수확한 농작물 합계 total 초기화
    total = 0
    # 2-2. 수확하지 않을 부분 rotten
    rotten = n // 2
    # 2-3. 수확 범위 fresh
    fresh = 1

    # 3-1. farm 모든 행을 순회
    row = 0
    while row < len(farm):
        # 3-2. rotten을 건너뛰고 fresh 만큼만 수확
        for i in range(fresh):
            total += int(farm[row][rotten + i])

        # 4. ◆ 모양대로 rotten / fresh 조정
        # 4-1. 현재 행이 중간보다 작으면 rotten ↓ fresh ↑
        if row < n // 2:
            rotten -= 1
            fresh += 2

        # 4-2. 현재 행이 중간보다 크면 rotten ↑ fresh ↓
        else:
            rotten += 1
            fresh -= 2

        row += 1

    return total


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())
    farm = [input() for _ in range(n)]
    print('#{} {}'.format(tc, harvest(n, farm)))