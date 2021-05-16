import sys
sys.stdin = open("input.txt")


def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    parent = [i for i in range(v+1)]

    result = 0
    edges.sort(key=lambda x:x[2])

    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2):
            union_set(n1, n2)
            result += w

    print("#{} {}".format(tc, result))

