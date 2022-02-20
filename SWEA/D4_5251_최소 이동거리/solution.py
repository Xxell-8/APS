import sys
sys.stdin = open('input.txt')


def bfs():
    distance, visited = [], []
    for _ in range(n+1):
        distance.append(10000000)
        visited.append(0)

    distance[0] = 0
    queue = [(distance[0], 0)]

    while queue:
        queue.sort(reverse=True)

        current_dist, current = queue.pop()
        visited[current] = 1

        if current == n:
            return current_dist

        for next, weight in graph[current]:
            if not visited[next] and distance[next] > current_dist + weight:
                distance[next] = current_dist + weight
                queue.append((distance[next], next))


T = int(input())
for tc in range(1, T + 1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    print('#{} {}'.format(tc, bfs()))