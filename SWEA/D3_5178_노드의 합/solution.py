# KEY > 무조건 순회할 생각부터 하지 말기..

import sys
sys.stdin = open('input.txt')


# 3. 트리를 완성하는 함수 생성
def node_sum(node):
    # 3-1. 노드 번호가 크기보다 크면 0
    if node > n:
        return 0
    # 3-2. 노드가 비어 있으면 자식 소환
    elif tree[node] == 0:
        tree[node] = node_sum(node*2) + node_sum(node*2+1)
        return tree[node]
    # 3-3. 노드 있으면 그냥 리턴
    else:
        return tree[node]


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, m, l = map(int, input().split())

    # 2. 트리 만들기
    tree = [0] * (n+1)
    for _ in range(m):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    # 4. 루트부터 시작
    node_sum(1)

    print('#{} {}'.format(tc, tree[l]))