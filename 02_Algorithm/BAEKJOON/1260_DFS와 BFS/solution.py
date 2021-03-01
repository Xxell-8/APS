import sys
sys.stdin = open('input.txt')

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    if graph[i]:
        graph[i] = sorted(graph[i], reverse=True)

# DFS
path = []
stack = [v]

while stack:
    current = stack.pop()
    if current not in path:
        path.append(current)
        stack += graph[current]

print(path)