import sys
sys.stdin = open('input.txt')

n = 100
for tc in range(1, 11):
    case_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    # 행 기준 sum
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += arr[i][j]
        if row_sum > result:
            result = row_sum

    # 열 기준 sum
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += arr[i][j]
        if col_sum > result:
            result = col_sum

    # 대각선 기준 sum
    diagonal_sum1 = 0
    diagonal_sum2 = 0
    for i in range(n):
        diagonal_sum1 += arr[i][i]
        diagonal_sum2 += arr[i][n - 1 - i]

    if diagonal_sum1 > result:
        result = diagonal_sum1
    if diagonal_sum2 > result:
        result = diagonal_sum2

    print('#{} {}'.format(tc, result))