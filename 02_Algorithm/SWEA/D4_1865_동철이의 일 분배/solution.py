import sys
sys.stdin = open('input.txt')


def assign(task, percent):
    global result, selected

    if result >= percent * temp[task]:
        return

    if task == n:
        result = percent
        return

    for idx in range(n):
        if not selected[idx]:
            selected[idx] = 1
            assign(task + 1, percent * success[task][idx])
            selected[idx] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    success = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]

    temp = [max(success[x]) for x in range(n)] + [1]
    for i in range(n-2, -1, -1):
        temp[i] *= temp[i+1]

    result = 0
    selected = [0] * n

    assign(0, 1)
    print('#{} {:6f}'.format(tc, result * 100))