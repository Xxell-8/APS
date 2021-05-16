import sys
sys.stdin = open("input.txt")


def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)

    if rank[x] >= rank[y]:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    else:
        parent[x] = y


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    info = list(map(int, input().split()))

    parent = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]

    for i in range(m):
        union_set(info[2*i], info[2*i + 1])

    result = set()
    for i in range(1, n+1):
        result.add(find_set(i))

    print("#{} {}".format(tc, len(result)))

