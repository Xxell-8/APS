import sys
sys.stdin = open('input.txt')


def find_set(node):
    if parent[node] == node:
        return node
    return find_set(parent[node])


def union_set(root1, root2):
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


# 1. input 받기
N, M, K = map(int, input().split())
stations = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

# 2-1. Kruskal 활용을 위해 간선 정보 가중치 기준으로 정렬
edges.sort(key=lambda x: x[2])

# 2-2. 부모 정보 초기화
parent = [i for i in range(N+1)]
# 2-3. 발전소는 0을 부모로 설정하여 union 해주기
for station in stations:
    parent[station] = 0

# 2-4. result 변수 초기화
result = 0

# 3-1. 간선 정보를 순회하며,
for u, v, w in edges:
    # 3-2. 두 노드의 루트가 다를 경우,
    root_u = find_set(u)
    root_v = find_set(v)
    if root_u != root_v:
        # 3-3. 루트를 합쳐주고 result에 비용 추가
        union_set(root_u, root_v)
        result += w

print(result)