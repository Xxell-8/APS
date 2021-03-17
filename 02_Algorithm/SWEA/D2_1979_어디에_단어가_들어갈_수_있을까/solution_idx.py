import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. input 받기
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    # 2. 결과 값을 담을 result 초기화
    result = 0

    # 3-1. puzzle 탐색
    for i in range(n):
        # 3-2. 가로 빈 칸 / 세로 빈 칸
        row_blank = 0
        col_blank = 0
        for j in range(n):
            # 3-3. 가로 빈 칸 확인
            if puzzle[i][j] == 1:
                row_blank += 1
            elif puzzle[i][j] == 0:
                if row_blank == k:
                    result += 1
                row_blank = 0

            # 3-4. 세로 빈 칸 확인
            if puzzle[j][i] == 1:
                col_blank += 1
            elif puzzle[j][i] == 0:
                if col_blank == k:
                    result += 1
                col_blank = 0

        if row_blank == k:
            result += 1

        if col_blank == k:
            result += 1

    print('#{} {}'.format(tc, result))