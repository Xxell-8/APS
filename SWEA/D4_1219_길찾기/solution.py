import sys
sys.stdin = open('input.txt')


def route99(graph):
    # 2. 방문 체크 및 스택 생성
    visited = [0] * 100
    to_go = [0]

    # 3. 갈 곳이 남아있는 동안 탐색
    while to_go:
        current = to_go.pop()

        # 4. 목적지에 도착하면 리턴
        if current == 99:
            return 1

        # 5-1. 방문하지 않은 곳이면,
        if not visited[current]:
            # 5-2. 방문 체크하고
            visited[current] = 1

            # 5-3. 다음 방문지 확인
            for node in graph[current]:
                if not visited[node]:
                    to_go.append(node)
    # 6. 목적지에 도착 못하고 탐색 종료시 0
    return 0


T = 10
for _ in range(1, T + 1):
    # 1. input 받기
    tc, n = map(int, input().split())
    a, b = 0, 99
    graph = [[] for _ in range(100)]
    edge = list(map(int, input().split()))

    for idx in range(0, n * 2, 2):
        s, e = edge[idx], edge[idx+1]
        graph[s].append(e)

    print('#{} {}'.format(tc, graph, route99(graph)))