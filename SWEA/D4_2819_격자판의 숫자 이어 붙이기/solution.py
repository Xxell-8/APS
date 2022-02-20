import sys
sys.stdin = open('input.txt')


def make_number(row, col, num):
    # 4-1. num에 현재 위치 값을 추가
    num += grid[row][col]

    # 5. num이 7 자리가 되면 result에 추가하고 종료
    if len(num) == 7:
        result.add(num)
        return

    # 4-2. 현재 위치에서 4방향 탐색
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc
        # 4-3. 갈 수 있는 위치라면
        if 0 <= nr < 4 and 0 <= nc < 4:
            # 4-4. 해당 지점에서 다시 시작
            make_number(nr, nc, num)


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    grid = [list(input().split()) for _ in range(4)]

    # 2. 결과값 중복 제거를 위해 set()으로 생성
    result = set()

    # 3. 모든 지점에서 탐색 시작
    for i in range(4):
        for j in range(4):
            make_number(i, j, '')

    print('#{} {}'.format(tc, len(result)))