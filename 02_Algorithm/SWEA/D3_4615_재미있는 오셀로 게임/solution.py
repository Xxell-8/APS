import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. input 받고
    n, m = map(int, input().split())
    # 2-1. index 맞추기 위해서 테두리 추가
    board = [[0 for _ in range(n+2)] for _ in range(n+2)]
    c = (n+2) // 2
    # 2-2. 정가운데 돌 배치 > 게임 기본 세팅
    for i in range(c-1, c+1):
        board[i][i] = 2
        board[i][n+1-i] = 1

    # 3. m번 동안 반복
    for _ in range(m):
        x, y, color = map(int, input().split())
        # 4. 해당 위치에 돌을 놓고
        board[y][x] = color

        # 5-1. 주변 8방향 탐색
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # 5-2. 탐색한 칸이 0이 아니고, 상대편 돌이면,
                if board[y+i][x+j] and board[y+i][x+j] != color:
                    # 5-3. 해당 방향으로 전진
                    row, col = i, j
                    cnt = 0
                    change = False
                    while 0 < y+row <=n and 0 < x+col <= n:
                        cnt += 1
                        # 6-1. 전진한 칸이 0이면 바꿀 게 없음 > break
                        if not board[y+row][x+col]:
                            break
                        # 6-2. 전진한 칸이 내 돌이면 거기까지 바꿀 수 있음 > break
                        elif board[y+row][x+col] == color:
                            change = True
                            break
                        row += i
                        col += j

                    # 6-3. 바꿀 수 있으면 내 돌이 나오기 전까지 다 내 돌로 바꾸기
                    if change:
                        for step in range(1, cnt):
                            board[y + i*step][x + j*step] = color

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