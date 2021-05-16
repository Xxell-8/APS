import sys
sys.stdin = open('input.txt')


def calculate(node):

    if tree[node][0].isdigit():
        return int(tree[node][0])

    else:
        x = calculate(int(tree[node][1]))
        y = calculate(int(tree[node][2]))

        if tree[node][0] == '+':
            return x + y
        elif tree[node][0] == '-':
            return x - y
        elif tree[node][0] == '*':
            return x * y
        elif tree[node][0] == '/':
            return x / y

T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N):
        info = input().split()
        key = int(info[0])
        tree[key] += info[1:]

    print('#{} {}'.format(tc, int(calculate(1))))