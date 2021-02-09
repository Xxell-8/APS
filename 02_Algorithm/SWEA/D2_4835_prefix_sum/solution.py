import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    prefix_sum = []
    for i in range(n-m+1):
        prefix = 0
        for j in range(m):
            prefix += nums[i+j]
        prefix_sum.append(prefix)

    maximum = prefix_sum[0]
    minimum = prefix_sum[0]
    for ps in prefix_sum:
        if ps > maximum:
            maximum = ps
        elif ps < minimum:
            minimum = ps
    result = maximum - minimum

    print('#{} {}'.format(tc, result))
