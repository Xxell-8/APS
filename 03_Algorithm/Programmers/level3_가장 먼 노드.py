def solution(n, edge):
    # 1. 그래프 연결 정보 저장
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a] += [b]
        graph[b] += [a]

    # 2-1. 1번 노드로부터 떨어진 거리를 계산할 distance 초기화
    distance = [0 for _ in range(n + 1)]
    distance[1] = 1
    # 2-2. 갈 수 있는 노드를 큐에 담고
    q = [1]

    # 3-1. 갈 수 있는 노드가 있으면,
    while q:
        # 3-2. 현재 위치 잡고
        current = q.pop(0)
        # 3-3. 갈 수 있는 노드들을 보면서
        for next in graph[current]:
            # 3-4. 방문한 적이 없다면(거리 계산을 안했다면)
            if not distance[next]:
                # 3-5. 거리 계산하고 큐에 추가
                distance[next] = distance[current] + 1
                q.append(next)

    # 4. 최대 거리가 몇 개인지 반환
    return distance.count(max(distance))