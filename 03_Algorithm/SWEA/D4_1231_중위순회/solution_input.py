import sys
sys.stdin = open('input.txt')


# 3. 중위순회 함수 생성
def inorder(node):
    if len(tree[node]) > 1:
        inorder(tree[node][1])
    result.append(tree[node][0])
    if len(tree[node]) > 2:
        inorder(tree[node][2])


for tc in range(1, 11):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n):
        # 1-1. info 길이가 다르기 때문에 통으로 받고
        info = input().split()
        # 1-2. 공통정보(노드 번호, 정보) 저장
        node_no = int(info[0])
        tree[node_no].append(info[1])
        # 1-3. 연결 정보 있는지 확인 후 있으면 저장
        if len(info) > 2:
            tree[node_no].append(int(info[2]))
            if len(info) > 3:
                tree[node_no].append(int(info[3]))

    # 2. 결과값 담을 리스트 생성
    result = []
    inorder(1)
    print('#{} {}'.format(tc, ''.join(result)))