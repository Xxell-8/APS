import sys
sys.stdin = open('input.txt')


def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_root(x)
    root_y = find_root(y)

    if root_x > root_y:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    parent = list(range(N+1))
    for i in range(M):
        n1, n2 = info[2*i], info[2*i+1]
        union(n1, n2)

    result = set()
    for i in range(1, N+1):
        result.add(find_root(i))

    print('#{} {}'.format(tc, len(result)))