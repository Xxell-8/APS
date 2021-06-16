import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    # 1-1. 결과 값 result 기본 세팅
    result = [[1]]

    # 1-2. (stack 활용) 직전 행의 숫자 추가 + 양 끝은 0이라고 가정
    last = [0, 1]

    # 2-1. n번째 줄까지 반복
    for current in range(1, n):
        # 2-2. 현재 줄에 추가할 숫자 계산 nums
        nums = []
        left = 0
        while last:
            right = last.pop()
            # 2-3. 왼쪽/오른쪽 위의 숫자 합 계산
            nums.append(left + right)
            # 2-4. 한 칸 이동
            left = right

        # 3-1. 현재 행 last/result 추가
        # 파스칼의 삼각형은 좌우 대칭이라서 순서를 신경쓰지 않아도 된다.
        last += [0] + nums
        result.append(nums)

    print('#{}'.format(tc))
    for row in result:
        print(' '.join([str(num) for num in row]))