import sys
sys.stdin = open('input.txt')


def solution(M):
    N = len(M)
    nxt = 'U'
    y = N - 1
    for x in range(N):
        last_row = M[y]
        if last_row[x] == 2:
            while y > 0:
                if nxt == 'U':
                    if x < N-1 and M[y][x+1]:
                        nxt = 'R'
                        x += 1
                    elif x > 0 and M[y][x-1]:
                        nxt = 'L'
                        x -= 1
                    else:
                        y -= 1
                else:
                    if M[y-1][x]:
                        nxt = 'U'
                        y -= 1
                    elif nxt == 'R':
                        x += 1
                    elif nxt == 'L':
                        x -= 1
            return x


N = 100
for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, solution(matrix)))