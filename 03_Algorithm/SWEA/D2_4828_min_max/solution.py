import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. 주어진 숫자를 받고
    n = int(input())
    nums = list(map(int, input().split()))

    # 2. max/min 변수를 만들고
    maximum = nums[0]
    minimum = nums[0]

    # 3. nums를 순회하면서 max/min 값을 찾기
    for num in nums:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num

    result = maximum - minimum
    print('#{} {}'.format(tc, result))