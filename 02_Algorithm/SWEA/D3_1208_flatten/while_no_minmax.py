import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    nums = list(map(int, input().split()))

    while n:
        maximum = nums[0]
        minimum = nums[0]
        max_idx = 0
        min_idx = 0

        for idx in range(len(nums)):
            if nums[idx] > maximum:
                maximum = nums[idx]
                max_idx = idx

            elif nums[idx] < minimum:
                minimum = nums[idx]
                min_idx = idx

        nums[max_idx] -= 1
        nums[min_idx] += 1
        n -= 1

    maximum_final = nums[0]
    minimum_final = nums[0]
    for num in nums:
        if num > maximum_final:
            maximum_final = num

        elif num < minimum_final:
            minimum_final = num
    result = maximum_final - minimum_final

    print('#{} {}'.format(tc, result))