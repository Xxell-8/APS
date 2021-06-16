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
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    info.sort(key=lambda x:x[2])

    parent = [i for i in range(V+1)]
    result = 0
    for n1, n2, w in info:
        if find_root(n1) != find_root(n2):
            union(n1, n2)
            result += w


    print('#{} {}'.format(tc, result))