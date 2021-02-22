import sys
sys.stdin = open('input.txt')


def rotation(nums, n):
    result = [[0 for _ in range(3)] for _ in range(n)]

    for i in range(n):
        num_90 = ''
        num_180 = ''
        num_270 = ''
        for j in range(n):
            # 90
            num_90 += nums[(n - 1) - j][i]
            # 180
            num_180 += nums[(n - 1) - i][(n - 1) - j]
            # 270
            num_270 += nums[j][(n - 1) - i]

        result[i][0] = num_90
        result[i][1] = num_180
        result[i][2] = num_270

    return result


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = [list(input().split()) for _ in range(n)]
    print('#{}'.format(tc))

    result = rotation(nums, n)
    for nums in result:
        for num in nums:
            print(num, end=" ")
        print()