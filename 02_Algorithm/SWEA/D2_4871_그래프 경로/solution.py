import sys
sys.stdin = open('input.txt')


def s_to_g(v, graph, s, g):
    visited = [0] * (v + 1)
    stack = [s]
    while stack:
        current = stack.pop()
        if current == g:
            return 1

        if not visited[current]:
            visited[current] = 1
            for node in graph[current]:
                if not visited[node]:
                    stack.append(node)
    return 0


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    s, g = map(int, input().split())

    print('#{} {}'.format(tc, s_to_g(v, graph, s, g)))