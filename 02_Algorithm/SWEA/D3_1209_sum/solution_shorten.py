import sys
sys.stdin = open('input.txt')


def solution(N, matrix):
    maximum = 0
    row_sum = col_sum = x1_sum = x2_sum = 0

    for i in range(N):
        x1_sum += matrix[i][i]
        x2_sum += matrix[i][N-1-i]

        for j in range(N):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

        if row_sum > maximum:
            maximum = row_sum
        if col_sum > maximum:
            maximum = col_sum
        row_sum = col_sum = 0

    if x1_sum > maximum:
        maximum = x1_sum
    if x2_sum > maximum:
        maximum = x2_sum

    return maximum


for _ in range(1, 11):
    N = 100
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = solution(N, matrix)
    print('#{} {}'.format(tc, result))