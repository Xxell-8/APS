import sys
sys.stdin = open('input.txt')


def shortest():
    # 4-1. 갈 수 있는 노드가 남아있는 동안,
    while queue:
        # 4-2. 현재 위치를 찍고 방문 체크
        current = queue.pop(0)
        visited[current] = 1

        # 4-3. 현재 위치와 인접한 노드를 보면서
        for next in graph[current]:
            # 4-4. 방문하지 않은 곳이면
            if not visited[next]:
                # 4-5. 방문 체크 + 거리 기록 + queue에 추가
                visited[next] = 1
                distance[next] = distance[current] + 1
                queue.append(next)


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())

    # 2-1. 방문 체크할 visited 초기화
    visited = [0] * (v+1)
    # 2-2. 출발 노드로부터의 거리를 기록할 distance 초기화
    distance = [0] * (v+1)
    # 2-3. 시작점을 담은 queue
    queue = [s]

    # 3. 최단 거리 찾기
    shortest()

    print('#{} {}'.format(tc, distance[g]))