import sys
sys.stdin = open('input.txt')


def find_chemicals():
    def is_chemical(r, c):
        return 0 <= r < n and 0 <= c < n and bunker[r][c]

    def chemical_box(i, j):
        r, c = i, j
        # 마지막 행 확인
        while is_chemical(r, c):
            r += 1
        row_len = r - i

        while is_chemical(r-1, c):
            c += 1
        col_len = c - j

        for row in range(i, r):
            for col in range(j, c):
                bunker[row][col] = 'C'

        return [row_len, col_len]

    chemicals = []
    for i in range(n):
        for j in range(n):
            if bunker[i][j] and bunker[i][j] != 'C':
                chemicals += [chemical_box(i, j)]

    return sorted(chemicals, key=lambda x: (x[0] * x[1], x[0]))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    bunker = [list(map(int, input().split())) for _ in range(n)]
    result = find_chemicals()
    print('#{} {}'.format(tc, len(result)), end=' ')
    for box in result:
        for num in box:
            print(num, end=' ')
    print()