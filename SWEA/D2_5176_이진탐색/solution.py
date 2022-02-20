import sys
sys.stdin = open('input.txt')


# 3. 이진탐색트리 만드는 함수 생성
def bin_tree(node):
    global num
    # 3-1. 노드 번호가 n보다 크면 종료
    if node > n:
        return

    # 3-2. 좌 > 중앙 > 우 순으로 순회
    bin_tree(node * 2)
    # 3-3. 해당하는 자리에 숫자를 넣고, +1 해주기
    tree[node] = num
    num += 1
    bin_tree(node * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())

    # 2. 필요한 변수 생성
    tree = [0] * (n + 1)
    num = 1

    # 4. root(1)부터 시작
    bin_tree(1)

    # 5. 루트, n//2 자리 숫자 출력
    print('#{} {} {}'.format(tc, tree[1], tree[n//2]))