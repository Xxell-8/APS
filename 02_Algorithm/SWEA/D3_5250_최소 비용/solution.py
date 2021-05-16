import sys
sys.stdin = open("input.txt")


def sol(matrix):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    inf = n * n * 1000
    distance = [[inf for _ in range(n)] for _ in range(n)]

    check = [(0, 0)]
    distance[0][0] = 0

    while check:
        row, col = check.pop(0)
        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < n and 0 <= nc < n:
                diff = 0
                if matrix[nr][nc] > matrix[row][col]:
                    diff = matrix[nr][nc] - matrix[row][col]

                if distance[nr][nc] > distance[row][col] + diff + 1:
                    distance[nr][nc] = distance[row][col] + diff + 1
                    check.append((nr, nc))

    return distance[n-1][n-1]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    energy = [list(map(int, input().split())) for _ in range(n)]

    print("#{} {}".format(tc, sol(energy)))

