import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 1. 주어진 숫자를 받아오고
    n = int(input())
    nums = list(map(int, input().split()))

    # 2. n이 0이 될 때까지
    while n:
        # 3. nums의 max/min을 구해서
        max_idx = 0
        min_idx = 0

        for idx in range(len(nums)):
            if nums[idx] > nums[max_idx]:
                max_idx = idx

            elif nums[idx] < nums[min_idx]:
                min_idx = idx
        
        # 4. max 값은 하나 빼고 min 값은 하나 더한다
        nums[max_idx] -= 1
        nums[min_idx] += 1
        n -= 1

        # 차이가 0이나 1인지 확인
        max_idx = 0
        min_idx = 0

        for idx in range(len(nums)):
            if nums[idx] > nums[max_idx]:
                max_idx = idx

            elif nums[idx] < nums[min_idx]:
                min_idx = idx

        diff = nums[max_idx] - nums[min_idx]
        if diff == 0 or diff == 1:
            result = diff
            break
    
    # 5. n번 만큼 반복이 끝나면, 최종적인 max/min의 차이를 구한다
    maximum_final = nums[0]
    minimum_final = nums[0]
    for num in nums:
        if num > maximum_final:
            maximum_final = num

        elif num < minimum_final:
            minimum_final = num
    result = maximum_final - minimum_final

    print('#{} {}'.format(tc, result))