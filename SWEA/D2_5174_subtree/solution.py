import sys
sys.stdin = open('input.txt')

# KEY > 노드 개수를 구하는 문제이기 때문에 순회 순서는 상관 없음


# 4. 서브트리 함수 생성
def subtree(n):
    # 4-1. 자신부터 추가하고
    result.append(n)

    # 4-2. 자식이 있는지 확인 > 없으면 종료
    if not tree[n]:
        return

    # 4-3. 자식들 확인해서 있는 만큼 자손 확인
    for next in tree[n]:
        subtree(next)


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    e, n = map(int, input().split())
    edge = list(map(int, input().split()))

    # 2. 2차원 리스트로 tree 구조 만들기
    tree = [[] for _ in range(e+2)]
    for i in range(e):
        p, c = edge[2*i], edge[2*i+1]
        tree[p].append(c)

    # 3. 서브트리의 node를 기록할 result 생성
    result = []
    subtree(n)
    print('#{} {}'.format(tc, len(result)))