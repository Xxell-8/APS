import sys
sys.stdin = open('input.txt')


def cal_tree(node):
    if not tree[node][0]:
        return 0
    elif type(tree[node][0]) == str:
        if tree[node][0] == '+':
            tree[node][0] = cal_tree(tree[node][1]) + cal_tree(tree[node][2])
        elif tree[node][0] == '-':
            tree[node][0] = cal_tree(tree[node][1]) - cal_tree(tree[node][2])
        elif tree[node][0] == '/':
            tree[node][0] = cal_tree(tree[node][1]) / cal_tree(tree[node][2])
        elif tree[node][0] == '*':
            tree[node][0] = cal_tree(tree[node][1]) * cal_tree(tree[node][2])
        return tree[node][0]
    else:
        return tree[node][0]

for tc in range(1, 11):
    n = int(input())
    tree = [[0 for _ in range(3)] for _ in range(n+1)]
    for _ in range(n):
        info = input().split()
        idx = int(info[0])
        val = int(info[1]) if info[1].isdigit() else info[1]

        tree[idx][0] = val
        tree[idx][1] = int(info[2]) if len(info) > 2 else 0
        tree[idx][2] = int(info[3]) if len(info) > 3 else 0


    cal_tree(1)
    print('#{} {}'.format(tc, int(tree[1][0])))
