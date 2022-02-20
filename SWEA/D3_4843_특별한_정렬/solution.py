import sys
sys.stdin = open('input.txt')

# KEY > 선택 정렬 활용

T = int(input())
for tc in range(1, T+1):
    # 1. 주어진 input을 받고
    n = int(input())
    nums = list(map(int, input().split()))

    # 2. 마지막 요소를 제외한 나머지를 순회
    for i in range(n-1):
        # 3-1. 인덱스가 짝수이면 max 선택
        if i % 2 == 0:
            max_idx = i
            # 3-2. 좌측은 정렬된 상태이기 때문에 우측만 순회
            for j in range(i+1, n):
                if nums[max_idx] < nums[j]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

        # 4. 홀수이면 min 선택 > 3과 같은 방식으로 선택 정렬
        else:
            min_idx = i
            for j in range(i+1, n):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    result = ' '.join([str(nums[i]) for i in range(10)])

    print('#{} {}'.format(tc, result))