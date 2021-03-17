import sys
sys.stdin = open('input.txt')


def delicious_diet(idx, taste, calorie):
    global result

    # 3. 칼로리가 제한선을 넘으면
    if calorie > l:
        return

    # 4. 마지막 재료까지 확인하면 점수 확인
    if idx == n:
        if taste > result:
            result = taste
        return

    # 재료 넣고 다음 재료 확인
    delicious_diet(idx+1, taste + info[idx][0], calorie + info[idx][1])
    # 넣은 재료 빼고 다음 재료 확인
    delicious_diet(idx+1, taste, calorie)


T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, l = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    # 2. result 초기화
    result = 0

    delicious_diet(0, 0, 0)

    print('#{} {}'.format(tc, result))
