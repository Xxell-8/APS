import sys
sys.stdin = open('input.txt')

# KEY > 맨 위에 있는 블럭의 낙차가 해당 블럭의 열에서 제일 크다
## 오른쪽으로 90도 회전할 때, 해당 블럭의 오른쪽만 확인하면 된다
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    # 1. result 초기화
    result = 0
    for i in range(len(nums)):
        # 2. 각 열의 낙차 drop 초기화
        drop = 0
        # 3-1. 해당 열의 오른쪽을 순회
        for j in range(i, len(nums)):
            # 3-2. 해당 열이 더 높으면 한 칸 떨어지므로 +1
            if nums[i] > nums[j]:
                drop += 1
        # 4. drop의 최댓값을 result에 할당
        if drop > result:
            result = drop
    print('#{} {}'.format(tc, result))
