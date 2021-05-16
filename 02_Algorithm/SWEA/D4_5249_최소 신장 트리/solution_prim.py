import sys
sys.stdin = open('input.txt')


def prim(graph):
    key, pi, visited = [], [], []
    for _ in range(v + 1):
        key.append(11)
        pi.append(None)
        visited.append(0)

    key[0] = 0
    for _ in range(v+1):
        min_idx = -1
        min_key = 11
        for i in range(v+1):
            if not visited[i] and key[i] < min_key:
                min_key = key[i]
                min_idx = i

        visited[min_idx] = 1
        for node, weight in graph[min_idx]:
            if not visited[node] and weight < key[node]:
                key[node] = weight
                pi[node] = min_idx

    return sum(key)


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = {}

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        graph[n1] = graph.get(n1, []) + [(n2, w)]
        graph[n2] = graph.get(n2, []) + [(n1, w)]


    print('#{} {}'.format(tc, prim(graph)))