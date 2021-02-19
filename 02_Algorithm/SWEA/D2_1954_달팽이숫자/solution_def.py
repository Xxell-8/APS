import sys
sys.stdin = open('input.txt')


def solution(N):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    x = y = 0
    move = 1

    for i in range(N, 0, -1):
        for k in range(i):
            matrix[y][x] = num
            num += 1
            if k == i - 1:
                y += move
            else:
                x += move

        for k in range(i-1):
            matrix[y][x] = num
            num += 1
            if k == i -2:
                move *= -1
                x += move
            else:
                y += move
    return '\n'.join([' '.join(map(str, row)) for row in matrix])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = solution(N)
    print('#{}\n{}'.format(tc, result))