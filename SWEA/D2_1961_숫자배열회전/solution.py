import sys
sys.stdin = open('input.txt')


def rotation(nums, n):
    # 2. 90, 180, 270도 회전한 행렬을 담을 result 초기화
    result = [[0 for _ in range(3)] for _ in range(n)]

    # 3. n의 범위를 순회
    for i in range(n):
        num_90 = ''
        num_180 = ''
        num_270 = ''
        for j in range(n):
            # 4-1. 90도 회전은 거꾸로 j, i
            num_90 += nums[(n - 1) - j][i]
            # 4-2. 180도 회전은 거꾸로 i, 거꾸로 j
            num_180 += nums[(n - 1) - i][(n - 1) - j]
            # 4-3. 270도 회전은 j, 거꾸로 i
            num_270 += nums[j][(n - 1) - i]

        # 5. 순서대로 result에 추가
        result[i][0] = num_90
        result[i][1] = num_180
        result[i][2] = num_270

    return result


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받기
    n = int(input())
    nums = [list(input().split()) for _ in range(n)]
    print('#{}'.format(tc))

    # 1-2. 회전한 배열 받아오기
    result = rotation(nums, n)
    for nums in result:
        for num in nums:
            print(num, end=" ")
        print()