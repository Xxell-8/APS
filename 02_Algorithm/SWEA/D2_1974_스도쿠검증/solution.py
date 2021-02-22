import sys
sys.stdin = open('input.txt')


def sudoku_check(puzzle):
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            # 가로 확인
            if puzzle[i][j] in row:
                return 0
            else:
                row.append(puzzle[i][j])

            # 세로 확인
            if puzzle[j][i] in col:
                return 0
            else:
                col.append(puzzle[j][i])

    for row in [0, 3, 6]:
        for col in [0, 3, 6]:
            box = []
            for i in range(3):
                for j in range(3):
                    if puzzle[col + i][row + j] in box:
                        return 0
                    else:
                        box.append(puzzle[col + i][row + j])

    return 1


T = int(input())
for tc in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, sudoku_check(puzzle)))