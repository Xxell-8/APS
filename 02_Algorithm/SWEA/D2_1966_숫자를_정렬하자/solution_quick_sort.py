import sys
sys.stdin = open('input.txt')


def quick_sort(nums):
    if len(nums) < 2:
        return nums

    # 1. pivot 을 기준으로, 작으면 left 크면 right
    left, right = [], []
    pivot = nums[0]

    for idx in range(1, len(nums)):
        if nums[idx] < pivot:
            left.append(nums[idx])
        else:
            right.append(nums[idx])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return [*sorted_left, pivot, *sorted_right]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    print('#{} {}'.format(tc, quick_sort(numbers)))