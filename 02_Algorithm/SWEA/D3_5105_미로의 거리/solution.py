import sys
sys.stdin = open('input.txt')


def distance_of_maze(queue):
    # 3-1. 통로인지 확인
    def is_road(i, j):
        return 0 <= i < n and 0 <= j < n and not maze[i][j]
    # 3-2. 도착점인지 확인
    def is_goal(i, j):
        return 0 <= i < n and 0 <= j < n and maze[i][j] == 3

    # 4-1. 상하좌우 이동 좌표
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 4-2. 시작점부터 각 셀의 거리 기록
    distance = [[0 for _ in range(n)] for _ in range(n)]

    # 5. 이동할 수 있는 칸이 있을 때,
    while queue:
        # 6-1. 현재 위치 갱신 (BFS)
        now_i, now_j = queue.pop(0)
        # 6-2. 방문한 위치 표시
        maze[now_i][now_j] = 1

        # 7. 해당 위치에서 4방향 탐색
        for i, j in direction:
            next_i, next_j = now_i + i, now_j + j

            # 8-1. 이동할 수 있는 칸이 통로면,
            if is_road(next_i, next_j):
                # 8-2. 거리는 현재 칸 + 1
                distance[next_i][next_j] = distance[now_i][now_j] + 1
                # 8-3. queue에 경로 등록
                queue.append((next_i, next_j))

            # 9-1. 도착점이면 현재까지의 거리 return
            elif is_goal(next_i, next_j):
                return distance[now_i][now_j]

    return 0


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]

    # 2-1. queue 활용
    queue = []

    # 2-2. 시작점 찾아 queue에 추가
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                queue.append((i, j))

    print('#{} {}'.format(tc, distance_of_maze(queue)))