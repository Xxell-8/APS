import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 1. K, N, M, 충전기 위치를 각각 변수에 할당
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))

    # 2-1. 버스의 위치를 기록할 bus 변수 초기화
    bus = 0
    # 2-2. 이동 범위 내 충전소 위치를 기록할 next_charger 변수 초기화
    next_charger = 0
    # 2-3. 충전 횟수를 기록할 result 변수 초기화
    result = 0

    # 3. 버스가 도착점까지 갈 수 있는 지점(n-k)이 될 때까지
    while bus < n - k:
        # 4-1. 충전 없이 가장 멀리 갈 수 있는 정류장부터 탐색
        for stop in range(bus+k, bus, -1):
            # 4-2. 해당 정류장에 충전기가 있으면
            if stop in charger:
                # 4-3. 다음 충전소를 해당 정류장으로 바꾸고 break
                next_charger = stop
                break

        # 5-1. 이동가능한 범위에 충전소가 없으면 result=0
        if bus == next_charger:
            result = 0
            ## while 구문을 종료하기 위해 bus를 n으로 키워버리기
            bus = n

        # 5-2. 충전소가 있으면 버스를 해당 정류장으로 옮기고 result + 1
        else:
            bus = next_charger
            result += 1

    print('#{} {}'.format(tc, result))