import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. 주어진 숫자를 받아오고
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    # 2. 각각의 구간합을 prefix_sum에 추가
    prefix_sum = []
    for i in range(n-m+1):
        prefix = 0
        for j in range(m):
            prefix += nums[i+j]
        prefix_sum.append(prefix)

    # 3. 구간합이 담긴 list에서 max/min을 구하고
    maximum = prefix_sum[0]
    minimum = prefix_sum[0]
    for ps in prefix_sum:
        if ps > maximum:
            maximum = ps
        elif ps < minimum:
            minimum = ps

    # 4. max와 min의 차이를 result에 할당
    result = maximum - minimum

    print('#{} {}'.format(tc, result))
