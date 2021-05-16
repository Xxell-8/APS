import sys
sys.stdin = open('input.txt')


def max_prize(idx, cnt):
    if cnt == limit:
        result.append(int(''.join(nums)))
        return

    if idx == n:
        if (limit - cnt) % 2 and len(set(nums)) == n:
            nums[n-1], nums[n-2] = nums[n-2], nums[n-1]
        result.append(int(''.join(nums)))
        return

    current = nums[idx]
    max_card = max(nums[idx:])

    if current == max_card:
        max_prize(idx+1, cnt)
    else:
        for jdx in range(idx+1, n):
            if nums[jdx] == max_card:
                nums[idx], nums[jdx] = nums[jdx], nums[idx]
                max_prize(idx+1, cnt+1)
                nums[idx], nums[jdx] = nums[jdx], nums[idx]


T = int(input())
for tc in range(1, T + 1):
    info = input().split()
    nums = list(info[0])
    n = len(nums)
    limit = int(info[1])

    result = []
    max_prize(0, 0)
    print('#{} {}'.format(tc, max(result)))