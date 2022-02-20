import sys
sys.stdin = open('input.txt')


def binary_search(arr, left, right, target):
    global select

    # 2. 종료 조건 생성 > left-right가 교차하면 탐색 실패
    if left > right:
        return 0

    # 3-1. 중심 idx 설정
    center = (left + right) // 2

    # 3-2. target을 찾으면 return 1
    if arr[center] == target:
        return 1

    # 3-3. target이 중심 원소보다 작으면 좌측 탐색하는데,
    elif arr[center] > target:
        # 직전에도 좌측 탐색을 했으면 조건에 맞지 않으므로 return 0
        if select == 'left':
            return 0
        # 아니라면, 좌측 탐색 기록하고 탐색 시작
        select = 'left'
        return binary_search(arr, left, center - 1, target)

    # 3-4. target이 중심 원소보다 크면 같은 방식으로 우측 탐색
    else:
        if select == 'right':
            return 0
        select = 'right'
        return binary_search(arr, center + 1, right, target)


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받고
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    # 1-2. 조건에 맞는 원소 개수를 셀 result 초기화
    result = 0

    # 4-1. 리스트 b의 원소 중에
    for num in b:
        # 4-2. 리스트 a에 존재하는 원소만 이진 탐색
        if num in a:
            select = ''
            result += binary_search(a, 0, n - 1, num)

    print('#{} {}'.format(tc, result))