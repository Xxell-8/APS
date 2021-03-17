import sys
sys.stdin = open('input.txt')


def solution(v):
    dfs_path = []
    bfs_path = []
    queue = [v]

    def dfs(v):
        dfs_path.append(v)
        for edge in sorted(graph[v]):
            if edge not in dfs_path:
                dfs(edge)

    def bfs():
        if not queue:
            return

        current = queue.pop(0)
        if current not in bfs_path:
            bfs_path.append(current)
            queue.extend(sorted(graph[current]))
            bfs()
        else:
            bfs()

    dfs(v)
    bfs()

    return dfs_path, bfs_path



T = int(input())
for tc in range(1, T+1):
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print('#{} {}'.format(tc, solution(v)))