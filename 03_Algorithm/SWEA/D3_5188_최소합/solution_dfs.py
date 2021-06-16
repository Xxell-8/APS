import sys
sys.stdin = open('input.txt')


def bfs(i, j):
    dirs = [(1, 0), (0, 1)]

    q = [(i, j)]

    while q:
        row, col = q.pop(0)

        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < n and 0 <= nc < n:
                new = count[row][col] + board[nr][nc]
                if not count[nr][nc]:
                    count[nr][nc] = new
                elif new < count[nr][nc]:
                    count[nr][nc] = new
                bfs(nr, nc)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    count = [[0 for _ in range(n)] for _ in range(n)]
    count[0][0] = board[0][0]

    bfs(0, 0)
    print('#{} {}'.format(tc, count[n-1][n-1]))