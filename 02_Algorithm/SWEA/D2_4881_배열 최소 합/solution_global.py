import sys
sys.stdin = open('input.txt')


def minimum_sum(i):
    # 5. global에 위치한 result, tmp 사용
    global result, tmp

    # 7-1. 현재 tmp가 result 보다 크면 그만두기
    if tmp > result:
        return

    # 7-2. 끝까지 돌았는데, result보다 tmp가 작으면 최솟값 변경
    if i == n:
        if tmp < result:
            result = tmp
            return

    # 6-1. 범위 내의 열을 순회
    for j in range(n):
        # 6-2. 이전에 선택되지 않은 열이라면,
        if not selected[j]:
            # 6-3. 선택하고
            selected[j] = 1
            # 6-4. 해당 요소 tmp에 더하기
            tmp += arr[i][j]
            # 6-5. 다음 행 탐색
            minimum_sum(i + 1)

            # 8. 다시 돌아오면, 원상복구
            tmp -= arr[i][j]
            selected[j] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 1. 이미 선택한 열 기록
    selected = [0] * n
    # 2. 가능한 배열 합 계산
    tmp = 0
    # 3. tmp의 최솟값 저장
    result = n * 9

    # 4. 0번째 행부터 시작
    minimum_sum(0)

    print('#{} {}'.format(tc, result))