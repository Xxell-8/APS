import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    result = 0
    for i in range(len(nums)):
        drop = 0
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                drop += 1
        if drop > result:
            result = drop
    print('#{} {}'.format(tc, result))
