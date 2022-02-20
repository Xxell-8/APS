import sys
sys.stdin = open('input.txt')


def solution(N, matrix):
    # 2-1. 최댓값 maximum 초기화
    maximum = 0
    # 2-2. 각 행/열/대각선 합 초기화
    row_sum = col_sum = x1_sum = x2_sum = 0

    for i in range(N):
        # 3-1. x1(\), x2(/) 합계 계산
        x1_sum += matrix[i][i]
        x2_sum += matrix[i][N-1-i]

        # 3-2. 행/열 합계 계산
        for j in range(N):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

        # 3-3. 각각의 합계 비교 > 최댓값 구하기
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
    # 1. input 받기
    N = 100
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = solution(N, matrix)
    print('#{} {}'.format(tc, result))