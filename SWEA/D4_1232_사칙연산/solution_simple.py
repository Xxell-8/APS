# KEY > input은 2개 아니면 4개 (∵ 사칙연산)

import sys
sys.stdin = open('input.txt')


# 2. 계산하는 함수 생성
def cal_tree(node):
    # 2-1. node는 1부터 시작
    if node > 0:
        # 2-2. 좌우 자식 할당
        left = cal_tree(int(tree[node][1]))
        right = cal_tree(int(tree[node][2]))

        # 2-3. 숫자면 리턴
        if tree[node][0].isdigit():
            return int(tree[node][0])

        # 2-4. 연산이면 계산해서 저장
        else:
            if tree[node][0] == '+':
                tree[node][0] = left + right
            elif tree[node][0] == '-':
                tree[node][0] = left - right
            elif tree[node][0] == '/':
                tree[node][0] = left / right
            elif tree[node][0] == '*':
                tree[node][0] = left * right

            # 2-5. 계산된 값 리턴
            return int(tree[node][0])


for tc in range(1, 11):
    # 1. input 받기
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n):
        info = input().split()
        if len(info) == 2:
            tree[int(info[0])] += [info[1], 0, 0]
        else:
            tree[int(info[0])] += info[1:]

    cal_tree(1)
    print('#{} {}'.format(tc, int(tree[1][0])))
