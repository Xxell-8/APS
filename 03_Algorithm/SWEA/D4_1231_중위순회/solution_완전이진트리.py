import sys
sys.stdin = open('input.txt')

## KEY. input 형식 확인 > 완전이진트리 + root는 무조건 1
# 굳이 연결 정보를 저장하지 않고 계산 가능

# 2. 중위 순회 함수 생성
def inorder(node):
    # 2-1. 노드 번호가 n보다 크면 리턴
    if node > n:
        return
    # 2-2. 완전이진트리 특성 참고해서 좌 > 부모 > 우 순회
    inorder(node*2)
    result.append(tree[node])
    inorder(node*2 + 1)


for tc in range(1, 11):
    n = int(input())
    result = []

    # 1-1. 트리의 정보를 받을 리스트를 만들고
    tree = [0] * (n+1)
    for _ in range(n):
        # 1-2. 노드 번호와 알파벳을 받아 트리에 넣기
        info = input().split()
        tree[int(info[0])] = info[1]


    # 3. root는 무조건 1
    inorder(1)

    print('#{} {}'.format(tc, ''.join(result)))