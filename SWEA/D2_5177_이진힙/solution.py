import sys
sys.stdin = open('input.txt')


# 3. 최소힙으로 정렬해주는 함수 생성
def min_heap(idx):
    # 3-1. 부모 노드가 존재할 때만 정렬 진행
    if idx > 1:
        # 3-2. 부모 노드가 더 크면 자리 바꾸기
        if tree[idx] < tree[idx//2]:
            tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
            # 3-3. 그 위에도 확인
            min_heap(idx // 2)


# 4. 조상 노드 합계 구하는 함수 생성
def ancestor_sum(idx):
    result = 0
    while idx > 0:
        idx //= 2
        result += tree[idx]
    return result


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())
    nums = list(map(int, input().split()))

    # 2. 숫자 하나씩 추가하면서 정렬하기
    tree = [0]
    for num in nums:
        tree.append(num)
        idx = len(tree) - 1
        min_heap(idx)

    print('#{} {}'.format(tc, ancestor_sum(n)))