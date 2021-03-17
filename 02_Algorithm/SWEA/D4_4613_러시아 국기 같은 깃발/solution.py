import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]

    # 2. 각 행마다 해당 색으로 바꿀 때 칠해야 하는 칸의 개수 계산
    change = []
    for i in range(n):
        white = m - flag[i].count('W')
        blue = m - flag[i].count('B')
        red = m - flag[i].count('R')
        change.append([white, blue, red])

    # 3. 계산하기 쉽도록 누적합으로 변환
    for i in range(1, n):
        change[i][0] += change[i-1][0]
        change[i][1] += change[i-1][1]
        change[i][2] += change[i-1][2]

    # 4. 최솟값 계산을 위한 result 설정
    result = n * m

    # 5-1. W / B / R을 나누는 2개의 분기점 설정
    for i in range(n-2):
        for j in range(i+1, n-1):
            to_white = change[i][0]
            to_blue = change[j][1] - change[i][1]
            to_red = change[n-1][2] - change[j][2]

            # 5-2. 각 케이스의 합 중 최솟값 구하기
            tmp = to_white + to_blue + to_red
            if result > tmp:
                result = tmp

    print('#{} {}'.format(tc, result))