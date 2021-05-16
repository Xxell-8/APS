import sys
sys.stdin = open('input.txt')

dirs = [(1, 0), (0, 1)]

def move(row, col, total):
    global result

    total += matrix[row][col]

    if total >= result:
        return

    if row == N-1 and col == N-1:
        result = total
        return

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < N and 0 <= nc < N:
            move(nr, nc, total)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 100000
    move(0, 0, 0)

    print('#{} {}'.format(tc, result))