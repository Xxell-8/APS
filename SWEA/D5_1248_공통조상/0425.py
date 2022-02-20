import sys
sys.stdin = open('input.txt')


def find_common(x, y):
    ancestors = []
    result = 0

    def find_ancestor(node):
        if not parent[node]:
            return

        ancestors.append(parent[node])
        find_ancestor(parent[node])

    def common_ancestor(node):
        nonlocal result
        if parent[node] in ancestors:
            result = parent[node]
            return
        common_ancestor(parent[node])

    find_ancestor(x)
    common_ancestor(y)
    return result


def subtree(node):
    common_children.append(node)

    if not children[node]:
        return

    for next in children[node]:
        subtree(next)

T = int(input())
for tc in range(1, T + 1):
    V, E, x, y = map(int, input().split())
    info = list(map(int, input().split()))

    children = [[] for _ in range(V+1)]
    parent = [0 for _ in range(V+1)]
    for i in range(E):
        p, c = info[2*i], info[2*i+1]
        children[p].append(c)
        parent[c] = p

    common_ancestor = find_common(x, y)
    common_children = []
    subtree(common_ancestor)
    print('#{} {} {}'.format(tc, common_ancestor, len(common_children)))