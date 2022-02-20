import sys
sys.stdin = open('input.txt')


def make_binary(node):
    global num
    if node > N:
        return

    make_binary(node * 2)
    tree[node] = num
    num += 1
    make_binary(node * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    num = 1

    make_binary(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))