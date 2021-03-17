import sys
sys.stdin = open('input.txt')


def selection_sort(n, nums):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return ' '.join([str(num) for num in nums])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(tc, selection_sort(n, nums)))