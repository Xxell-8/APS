import sys
sys.stdin = open('input.txt')


def solution(N):
    matrix = [[] for _ in range(N)]
    for row in range(N):
        for col in range(row + 1):
            if col == 0 or col == row:
                matrix[row].append(1)

            else:
                upper_row = matrix[row-1]
                val = upper_row[col-1] + upper_row[col]
                matrix[row].append(val)

    return [map(str, row) for row in matrix]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    for n in solution(N):
        print(' '.join(n))