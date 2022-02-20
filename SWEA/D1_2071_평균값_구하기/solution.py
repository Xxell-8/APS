import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    total = 0
    for idx in range(len(nums)):
        total += nums[idx]

    result = round(total / len(nums))
    print('#{} {}'.format(tc, result))