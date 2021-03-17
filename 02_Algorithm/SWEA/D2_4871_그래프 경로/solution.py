import sys
sys.stdin = open('input.txt')


def s_to_g(v, graph, s, g):
    # 2-1. 방문한 노드를 체크할 visited 초기화
    visited = [0] * (v + 1)
    # 2-2. 갈 수 있는 곳을 담을 stack 기본 세팅
    stack = [s]

    # 3-1. 갈 수 있는 곳이 있으면,
    while stack:
        # 3-2. 현재 위치를 표시하는데,
        current = stack.pop()
        # 3-3. 현재 위치가 도착점이면 return
        if current == g:
            return 1

        # 3-4. 현재 위치를 온 적이 없으면,
        if not visited[current]:
            # 3-5. 방문 체크하고
            visited[current] = 1
            # 3-6. 현재 위치와 인접한 노드를 탐색
            for node in graph[current]:
                # 3-7. 방문하지 않은 곳만 stack에 추가
                if not visited[node]:
                    stack.append(node)
    return 0


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    s, g = map(int, input().split())

    print('#{} {}'.format(tc, s_to_g(v, graph, s, g)))