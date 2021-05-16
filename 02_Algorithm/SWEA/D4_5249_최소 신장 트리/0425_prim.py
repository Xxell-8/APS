import sys
sys.stdin = open('input.txt')


def prim():
    weight = [11] * (V+1)
    parent = [None] * (V+1)
    visited = [0] * (V+1)

    weight[0] = 0
    for _ in range(V+1):
        min_weight = 11
        for node in range(V+1):
            if not visited[node] and weight[node] < min_weight:
                min_weight = weight[node]
                next_node = node

        visited[next_node] = 1
        adj_nodes = graph[next_node]
        for node in range(V+1):
            w = adj_nodes[node]
            if not visited[node] and w and w < weight[node]:
                weight[node] = w
                parent[node] = next_node
    return sum(weight)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = graph[n2][n1] = w

    print('#{} {}'.format(tc, prim()))