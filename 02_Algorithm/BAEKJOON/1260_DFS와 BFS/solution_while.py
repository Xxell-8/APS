import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # DFS
    dfs = []
    stack = [v]

    while stack:
        current = stack.pop()
        if current not in dfs:
            dfs.append(current)
            stack += sorted(graph[current], reverse=True)

    # BFS
    bfs = []
    queue = [v]

    while queue:
        now = queue.pop(0)
        if now not in bfs:
            bfs.append(now)
            queue += sorted(graph[now])

    print('#{}\n{}\n{}'.format(tc, dfs, bfs))
