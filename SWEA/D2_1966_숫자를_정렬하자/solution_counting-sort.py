import sys
sys.stdin = open('input.txt')


def counting_sort(m):
    result = ''
    count = [0] * (m+1)
    for num in nums:
        count[num] += 1

    for i in range(m+1):
        result += (str(i) + ' ') * count[i]

    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    m = max(nums)

    print('#{} {}'.format(tc, counting_sort(m)))