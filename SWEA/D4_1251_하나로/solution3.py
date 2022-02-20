import sys
sys.stdin = open('test.txt')


def build():
    costs = [float('inf') for _ in range(n)]
    visited = [0 for _ in range(n)]

    costs[0] = 0
    queue = [(costs[0], 0)]
    result = []

    while queue:
        queue.sort(reverse=True)
        cost, current = queue.pop()
        visited[current] = 1

        for next, next_cost in graph[current]:
            if not visited[next] and costs[next] > next_cost:
                costs[next] = next_cost
                result.append([current, next, costs[next]])
                queue.append((costs[next], next))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    graph = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            graph[i].append((j, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))

    #print(graph)
    print('#{} {}'.format(tc, build()))