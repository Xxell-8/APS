import sys
sys.stdin = open('input.txt')

# 6. 경로 탐색 함수 생성
def find_way(current):
    # 7. 코드가 너무 길어져서 통로/목적지 판단하는 함수 생성
    def is_goal(next):
        return 0 <= next[0] < n and 0 <= next[1] < n and maze[next[0]][next[1]] == '3'
    def is_road(next):
        return 0 <= next[0] < n and 0 <= next[1] < n and maze[next[0]][next[1]] == '0'

    # 6-1. 현재 위치를 경로에 추가
    path.append(current)

    # 6-2. 도착지에 닿은 적이 없으면,
    if not arrival:
        # 6-3. 상하좌우를 확인
        for move in direction:
            next = (current[0] + move[0], current[1] + move[1])
            # 6-4. next가 경로에 없을 때
            if next not in path:
                # 6-5. next가 도착지면 arrival에 표시
                if is_goal(next):
                    arrival.append(1)
                    return
                # 6-6. next가 통로면 거기서부터 다시 탐색
                elif is_road(next):
                    find_way(next)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [input() for _ in range(n)]

    # 1-1. 지나온 경로 기록
    path = []
    # 1-2. 4방향 탐색
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 2. 도착점에 닿으면 append
    arrival = []

    # 3. 시작점 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                start = (i, j)
                break

    # 4. 시작점부터 탐색 시작
    find_way(start)

    # 5. 목적지에 도착했으면 1
    result = 1 if arrival else 0

    print('#{} {}'.format(tc, result))