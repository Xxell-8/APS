import sys
sys.stdin = open('input.txt')


# 1. 수평선의 오목을 확인할 함수 생성
def street_line(board):
    for line in board:
        if 'ooooo' in line:
            return True
    else:
        return False


# 2. 대각선의 오목을 확인할 함수 생성
## 대각선의 길이가 5인 경우만 확인
def diagonal(board, n):
    for i in range(n - 5 + 1):
        # 2-1. \ 선 확인
        for j in range(n - 5 + 1):
            count = 0
            for step in range(5):
                if board[i + step][j + step] == 'o':
                    count += 1
            if count == 5:
                return True
        # 2-2. / 선 확인
        for j in range(n - (n - 5) - 1, n):
            count = 0
            for step in range(5):
                if board[i + step][j - step] == 'o':
                    count += 1
            if count == 5:
                return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    # 3. 주어진 값을 받아오고
    n = int(input())
    row = [input() for _ in range(n)]
    # 4. zip() 활용 > 세로축을 가로로 변환
    col = [''.join(stone) for stone in zip(*row)]

    # 5. 값을 확인(가로, 세로, 대각선)
    if street_line(row):
        result = 'YES'
    elif street_line(col):
        result = 'YES'
    elif diagonal(row, n):
        result = 'YES'
    else:
        result = 'NO'

    print('#{} {}'.format(tc, result))
