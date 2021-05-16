import sys
sys.stdin = open('input.txt')


def build():
    costs = [float('inf') for _ in range(n)]
    visited = [0 for _ in range(n)]

    current = 0
    result = 0
    cnt = 0
    visited[0] = 1

    while cnt < n-1:
        min_idx = 0
        min_costs = float('inf')
        for i in range(n):
            if visited[i]:
                continue
            if costs[i] > graph[current][i]:
                costs[i] = graph[current][i]
            if costs[i] < min_costs:
                min_idx = i
                min_costs = costs[i]

        current = min_idx
        result += min_costs
        cnt += 1
        visited[min_idx] = 1
    return result * e


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    graph = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            graph[i][j] = graph[j][i] = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2


    print('#{} {}'.format(tc, build()))