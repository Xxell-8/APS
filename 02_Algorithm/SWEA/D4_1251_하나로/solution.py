import sys
sys.stdin = open('input.txt')


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
for tc in range(1, T + 1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            distance = (x[i]-x[j]) ** 2 + (y[i]-y[j]) ** 2
            edges.append((i, j, distance))

    edges.sort(key=lambda x:x[2], reverse=True)
    parent = [i for i in range(n)]
    result = []

    while edges:
        n1, n2, dist = edges.pop()
        if find_set(n1) != find_set(n2):
            union_set(n1, n2)
            result.append(dist * e)

        if len(result) == n-1:
            break

    print('#{} {}'.format(tc, round(sum(result))))