import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 가로 검색
    for i in range(n):
        blank = 0
        for j in range(n):
            if board[i][j] == 1:
                blank += 1
            elif board[i][j] == 0:
                if blank == k:
                    result += 1
                blank = 0
        if blank == k:
            result += 1


    # 세로 검색
    for j in range(n):
        blank = 0
        for i in range(n):
            if board[i][j] == 1:
                blank += 1
            elif board[i][j] == 0:
                if blank == k:
                    result += 1
                blank = 0
        if blank == k:
            result += 1

    print('#{} {}'.format(tc, result))