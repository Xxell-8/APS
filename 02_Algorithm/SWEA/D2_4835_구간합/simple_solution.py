import sys
sys.stdin = open('input.txt')

### solution.py에서 불필요한 작업 줄이기 ###
T = int(input())

for tc in range(1, T + 1):
    # 1. 주어진 숫자를 받아오고
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    # 2. 첫 번째 구간합을 계산
    prefix_sum = 0
    for i in range(m):
        prefix_sum += nums[i]

    # 3. 구간합의 max/min을 첫 번째 값으로 초기화
    max_sum = prefix_sum
    min_sum = prefix_sum

    # 4-1. 이미 계산한 첫 번째 구간을 제외하고 순회
    for i in range(m, n):
        # 4-2. 가장 먼저 추가된 수는 빼고, 새로운 수를 더해주기
        prefix_sum = prefix_sum + nums[i] - nums[i - m]

        # 4-3. max/min 값 판단
        if max_sum < prefix_sum:
            max_sum = prefix_sum
        elif min_sum > prefix_sum:
            min_sum = prefix_sum

    result = max_sum - min_sum

    print('#{} {}'.format(tc, result))