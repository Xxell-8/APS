import sys
sys.stdin = open('input.txt')


# 3. 주변 배추를 탐색하는 함수 생성
def dfs(row, col):
    # 3-1. 상하좌우 방향 저장
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    # 3-2. 탐색할 위치를 저장할 stack 초기화
    stack = [(row, col)]

    # 4-1. 탐색할 땅이 있으면,
    while stack:
        # 4-2. 현재 위치 기록하고
        cr, cc = stack.pop()
        # 4-3. 방문 체크를 위해 값을 바꾸기
        farm[cr][cc] = 2

        # 4-4. 현재 위치 기준으로 4방향으로 보면서
        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc
            # 4-5. 갈 수 있는 땅이고, 배추가 심어져 있으면
            if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] == 1:
                # 4-6. stack에 추가
                stack.append((nr, nc))


# 1. input 받기
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    # 2-1. 필요한 지렁이를 셀 answer 초기화
    answer = 0
    # 2-2. 배추 위치 정보가 들어 있는 farm을 순회하며
    for row in range(N):
        for col in range(M):
            # 2-3. 배추가 심어져 있으면, 주변 배추가 있는지 탐색
            if farm[row][col] == 1:
                dfs(row, col)
                # 5. 배추 구역 하나당 지렁이 한 마리 추가
                answer += 1

    print(answer)