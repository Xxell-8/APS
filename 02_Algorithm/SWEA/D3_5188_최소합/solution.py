import sys
sys.stdin = open('input.txt')


def min_sum():
    # 1. 맨 윗줄 + 맨 왼쪽 줄 계산하기
    for i in range(1, n):
        board[i][0] += board[i-1][0]
        board[0][i] += board[0][i-1]

    # 2-1. 남은 칸을 순회하면서
    for row in range(1, n):
        for col in range(1, n):
            # 2-2. 윗 칸과 좌측 칸의 값을 보고
            up = board[row-1][col]
            left = board[row][col-1]

            # 2-3. 더 작은 값을 불러와 더해주기
            if up < left:
                board[row][col] += up
            else:
                board[row][col] += left

    return board[n-1][n-1]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    print('#{} {}'.format(tc, min_sum()))