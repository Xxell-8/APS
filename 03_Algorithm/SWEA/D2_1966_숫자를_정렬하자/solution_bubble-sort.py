import sys
sys.stdin = open('input.txt')


def bubble_sort(n, nums):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return ' '.join([str(num) for num in nums])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(tc, bubble_sort(n, nums)))
