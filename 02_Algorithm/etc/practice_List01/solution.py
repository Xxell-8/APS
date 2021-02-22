import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # delta_ 상하좌우
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0

    for row in range(n):
        for col in range(n):
            for i in range(4):
                next_row = row + delta[i][0]
                next_col = col + delta[i][1]

                if 0 <= next_row < n and 0 <= next_col < n:
                    diff = abs(arr[next_row][next_col] - arr[row][col])
                    result += diff

    print("#{} {}".format(tc, result))
