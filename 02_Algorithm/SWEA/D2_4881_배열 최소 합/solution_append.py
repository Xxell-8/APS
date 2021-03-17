import sys
sys.stdin = open('input.txt')

# global 안 쓰고 풀기


def my_sum(row):
    # 6-1. 현재 tmp의 합이 result의 최소 합보다 크면 그만두기
    if result and sum(tmp) > min(result):
        return

    # 6-2. 마지막까지 돌았으면, tmp 합을 result에 추가
    if row == n:
        result.append(sum(tmp))
        return

    # 5-1. 범위 내의 열을 순회
    for col in range(n):
        # 5-2. 이전에 선택되지 않은 열이라면,
        if not selected[col]:
            # 5-3. 선택하고
            selected[col] = 1
            # 5-4. 해당 숫자를 tmp에 추가
            tmp.append(arr[row][col])
            # 5-5. 다음 행 탐색
            my_sum(row + 1)

            # 7. (원위치 시키기) 다시 돌아오면 현재 요소 빼고 선택 취소
            tmp.pop()
            selected[col] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 1. 이미 선택한 열 기록
    selected = [0] * n
    # 2. 가능한 배열 요소 기록
    tmp = []
    # 3. tmp의 합 기록
    result = []

    # 4. 0번째 행부터 시작
    my_sum(0)

    print('#{} {}'.format(tc, min(result)))