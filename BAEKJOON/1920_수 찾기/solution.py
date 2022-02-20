import sys
sys.stdin = open('input.txt')


# 3. 이분 탐색 함수 생성
def binary_search(start, end, target):
    # 3-1. 탐색할 구간이 있는 동안
    while start <= end:
        # 3-2. 가운데 값을 잡고
        mid = (start + end) // 2
        current = A[mid]

        # 3-3. 찾아야 하는 수와 같으면 1 반환
        if current == target:
            return 1

        # 3-4. 찾는 수보다 작으면 오른쪽 탐색
        if current < target:
            start = mid + 1
        # 3-5. 찾는 수보다 크면 왼쪽 탐색
        else:
            end = mid - 1
    # 3-6. 없으면 0 반환
    return 0


# 1. input 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# 2. 이분 탐색을 위해 A 정렬
A.sort()

# 4-1. 확인해야 하는 정수 x를 모두 순회하며
for x in nums:
    # 4-2. 이분 탐색 결과 출력
    print(binary_search(0, N-1, x))