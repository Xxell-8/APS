import sys
sys.stdin = open('input.txt')


def sudoku_check(sudoku):
    # 2. 스도쿠 퍼즐의 가로/세로 줄 확인
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            # 가로 확인
            if sudoku[i][j] in row:
                return 0
            else:
                row.append(sudoku[i][j])

            # 세로 확인
            if sudoku[j][i] in col:
                return 0
            else:
                col.append(sudoku[j][i])

    # 3. 3*3 격자 확인
    for row in [0, 3, 6]:
        for col in [0, 3, 6]:
            box = []
            for i in range(3):
                for j in range(3):
                    if sudoku[col + i][row + j] in box:
                        return 0
                    else:
                        box.append(sudoku[col + i][row + j])

    return 1


T = int(input())
for tc in range(1, T + 1):
    # 1. 스도쿠 퍼즐 받기
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, sudoku_check(sudoku)))