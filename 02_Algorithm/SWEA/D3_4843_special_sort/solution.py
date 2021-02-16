import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n-1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i+1, n):
                if nums[max_idx] < nums[j]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

        else:
            min_idx = i
            for j in range(i+1, n):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    result = ' '.join([str(nums[i]) for i in range(10)])

    print('#{} {}'.format(tc, result))