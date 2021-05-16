import sys
sys.stdin = open('input.txt')


def quick_sort(arr, start, end):
    # 2-1. 종료 조건 생성
    if start >= end:
        return

    # 2-2. 기본 idx 설정
    pivot = (start + end) // 2
    left = start
    right = end

    # 2-3. left와 right가 만날 때까지 반복
    while left < right:
        # 2-3. 왼쪽 원소가 기준값보다 작으면 우측으로 이동
        while arr[left] < arr[pivot] and left < right:
            left += 1
        # 2-4. 오른쪽 원소가 기준점보다 크면 좌측으로 이동
        while arr[right] >= arr[pivot] and left < right:
            right -= 1

        if left < right:
            # 3-1. pivot 기준 왼쪽 원소가 모두 pivot보다 작으면
            if left == pivot:
                # 3-2. pivot 변경
                pivot = right
            # 3-3. 조건에 맞지 않는 left, right 값을 swap
            arr[left], arr[right] = arr[right], arr[left]

    arr[pivot], arr[right] = arr[right], arr[pivot]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, n-1)
    #print(numbers)
    print('#{} {}'.format(tc, numbers[n//2]))