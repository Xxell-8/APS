import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    maximum = nums[0]
    minimum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num

    result = maximum - minimum
    print('#{} {}'.format(tc, result))