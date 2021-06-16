import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    n, m = map(int, input().split())

    # 2-1. board 초기화
    board = [[0 for _ in range(n)] for _ in range(n)]
    c = n // 2
    # 2-2. 정가운데 돌 배치 > 게임 기본 세팅
    for i in range(c-1, c+1):
        board[i][i] = 2
        board[i][(n-1)-i] = 1

    # 3. m번 동안 반복
    for _ in range(m):
        # 4-1. input 받아와서
        x, y, color = map(int, input().split())

        # 4-2. idx에 맞게 조정 후 해당 위치에 돌 놓기
        x -= 1
        y -= 1
        board[y][x] = color

        # 5-1. 주변 8방향 탐색
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                # 5-2. 현재 위치는 pass
                if dy == dx == 0:
                    continue

                # 5-3. 탐색할 칸의 좌표 계산
                next_y = y + dy
                next_x = x + dx

                # 5-4. 바꿀 수 있는지 체크
                change = False

                # 5-5. 몇 칸 바꿀 수 있는지 체크
                count = 0

                # 6-1. 보드 내에 탐색할 칸이 있고
                while 0 <= next_y < n and 0 <= next_x < n:
                    # 6-2. 상대편 돌이면 해당 방향으로 전진
                    if board[next_y][next_x] == 3 - color:
                        count += 1
                        next_y += dy
                        next_x += dx

                    # 6-3. 내 돌이 나오면 거기까지 바꿀 수 있음
                    elif board[next_y][next_x] == color:
                        count += 1
                        change = True
                        break

                    # 6-4. 빈 칸이면 탐색 중지
                    else:
                        break

                # 7. 바꿀 수 있으면 내 돌이 나오기 전까지 다 내 돌로 바꾸기
                if change:
                    for step in range(1, count):
                        board[y + dy * step][x + dx * step] = color

    # 7. 돌 세기
    black = 0
    white = 0
    for row in board:
        for stone in row:
            if stone == 1:
                black += 1
            elif stone == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))