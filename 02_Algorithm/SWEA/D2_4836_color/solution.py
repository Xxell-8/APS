import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [[0 for _ in range(10)] for _ in range(10)]
    # 1. 보라색이 된 칸을 count할 변수 생성
    purple = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        # 2-1. 주어진 영역만큼 색칠
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if board[i][j] == 0:
                    board[i][j] = color
                # 2-2. 이미 색칠이 되어 있으면 보라색이 되니까
                ## 조건상, 같은 색의 영역은 겹치지 않음
                else:
                    board[i][j] = 3
                    purple += 1

    print('#{} {}'.format(tc, purple))