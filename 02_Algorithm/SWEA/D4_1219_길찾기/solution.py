import sys
sys.stdin = open('input.txt')

def route99(graph):
    visited = [0] * 100
    to_go = [0]

    while to_go:
        current = to_go.pop()
        if current == 99:
            return 1

        if not visited[current]:
            visited[current] = 1

            for node in graph[current]:
                if not visited[node]:
                    to_go.append(node)
    return 0


T = 10
for _ in range(1, T + 1):
    tc, n = map(int, input().split())
    a, b = 0, 99
    graph = [[] for _ in range(100)]
    edge = list(map(int, input().split()))

    for idx in range(0, n * 2, 2):
        s, e = edge[idx], edge[idx+1]
        graph[s].append(e)

    print('#{} {}'.format(tc, graph, route99(graph)))