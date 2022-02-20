import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    D, A, B, F = map(int, input().split())

    # 2. result 초기화
    result = 0

    # 3. 파리의 이동 횟수 count 초기화
    count = 1

    # 4. 기차 간의 거리가 10^(-6) 이하가 될 때까지
    while D >= 10 ** (-6):
        # 5-1. A에서 B로 가는 경우
        if count % 2:
            t = D / (B + F)

        # 5-2. B에서 A로 가는 경우
        else:
            t = D / (A + F)

        # 6-1. 해당 시간만큼 파리가 날아간 거리 더하기
        result += F * t
        # 6-2. 해당 시간동안 줄어든 기차 사이 거리 계산
        D -= t * (A + B)
        # 6-3. 이동 횟수 +1
        count += 1

    print('#{} {}'.format(tc, result))