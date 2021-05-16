import sys
sys.stdin = open('input.txt')


def merge_sort(nums):
    global cnt

    # 2-1. 분할된 리스트 길이가 1이 되면 return
    if len(nums) < 2:
        return nums

    # 2-2. center를 기준으로 left-right 분할
    center = len(nums) // 2
    left = nums[0:center]
    right = nums[center:]

    # 2-3. left와 right를 각각 병합 정렬
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 3. 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 확인
    if sorted_left[-1] > sorted_right[-1]:
        cnt += 1

    # 4-1. 분할한 리스트를 병합할 merged 초기화
    merged = []

    # 4-2. 각각의 리스트를 순회하면서
    ldx = rdx = 0
    while ldx < len(sorted_left) and rdx < len(sorted_right):
        # 4-3. 왼쪽과 오른쪽 원소 비교 후 작은 값부터 merged에 추가
        if sorted_left[ldx] < sorted_right[rdx]:
            merged.append(sorted_left[ldx])
            ldx += 1
        else:
            merged.append(sorted_right[rdx])
            rdx += 1

    # 4-4. 남아있는 원소 merged 끝에 붙여주기
    merged += sorted_left[ldx:]
    merged += sorted_right[rdx:]

    return merged


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받고
    n = int(input())
    numbers = list(map(int, input().split()))

    # 1-2. 오른쪽 원소가 먼저 복사되는 경우의 수를 기록할 cnt 초기화
    cnt = 0

    # 5. 병합정렬한 numbers 받기
    sorted_numbers = merge_sort(numbers)

    print('#{} {} {}'.format(tc, sorted_numbers[n//2], cnt))