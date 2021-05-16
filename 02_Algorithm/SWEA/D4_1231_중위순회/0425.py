import sys
sys.stdin = open('input.txt')


def inorder(node):
    global answer

    if node > N:
        return

    inorder(2 * node)
    answer += tree[node]
    inorder(2 * node + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    for _ in range(N):
        info = input().split()
        node_no = int(info[0])
        node_val = info[1]
        tree[node_no] = node_val

    answer = ''
    inorder(1)
    print('#{} {}'.format(tc, answer))