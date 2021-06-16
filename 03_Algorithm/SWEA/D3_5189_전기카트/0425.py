import sys
sys.stdin = open('input.txt')


def perms(idx, n):
    global result

    def cal_energy(order):
        total = 0
        for i in range(N):
            start = order[i]
            end = order[i + 1]
            total += info[start][end]
        return total

    if idx == n-1:
        total = cal_energy([0] + order + [0])
        if total < result:
            result = total
        return

    for i in range(idx, n):
        order[idx], order[i] = order[i], order[idx]
        perms(idx+1, n)
        order[idx], order[i] = order[i], order[idx]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    order = list(range(1, N))
    result = 100 * N * N
    perms(0, len(order))

    print('#{} {}'.format(tc, result))