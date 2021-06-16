import sys
sys.stdin = open('input.txt')


def make_tree(node):
    if node > N:
        return 0

    if tree[node]:
        return tree[node]

    else:
        tree[node] = make_tree(node * 2) + make_tree(node * 2 + 1)
        return tree[node]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        key, val = map(int, input().split())
        tree[key] = val

    make_tree(1)

    print('#{} {}'.format(tc, tree[L]))