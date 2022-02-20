import sys
sys.stdin = open('input.txt')


def find_way(i, j):
    global result

    # 4-1. 목적지에 도착 못했으면 돌기
    if not result:
        # 4-2. 목적지에 도착하면 result = 1
        if maze[i][j] == 3:
            result = 1

        # 4-3. 목적지가 아니면
        else:
            # 4-4. 현재 위치 지났다는 표시
            maze[i][j] = 1
            # 4-5. 4방향 탐색
            dis = [-1, 1, 0, 0]
            djs = [0, 0, -1, 1]
            for idx in range(4):
                di, dj = dis[idx], djs[idx]
                # 4-6. 다음 위치가 범위 안에 있고 막힌 곳이 아니면,
                if 0 <= i + di < n and 0 <= j + dj < n:
                    if maze[i + di][j + dj] != 1:
                        # 4-7. 해당 위치에서 탐색
                        find_way(i + di, j + dj)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]

    # 1. 시작점 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = (i, j)
                break

    # 2. 목적지 도착 여부 확인
    result = 0
    # 3. 시작점부터 탐색 시작
    find_way(*start)

    print('#{} {}'.format(tc, result))