import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. 주어진 input 값 차례대로 처리
    # 1-1. 버스 노선 개수 n
    n = int(input())
    # 1-2. 각 버스 노선이 다니는 정류장의 범위 (a, b)
    bus_lines = []
    for _ in range(n):
        a, b = map(int, input().split())
        bus_lines.append((a, b))

    # 1-3. 버스 정류장의 개수 p
    p = int(input())
    # 1-4. 각 버스 정류장의 번호 c
    stop = []
    for _ in range(p):
        c = int(input())
        stop.append(c)

    # 2. 각 정류장을 지나는 버스 노선의 개수를 기록할 result 초기화
    result = [0] * p
    # 3. 버스 노선이 다니는 정류장의 범위를 기준으로
    for start, end in bus_lines:
        # 4. 각 정류장 번호를 확인하며
        for idx in range(len(stop)):
            # 5. 해당 정류장이 범위 안에 있으면 +1
            if stop[idx] in range(start, end+1):
                result[idx] += 1

    result = ' '.join([str(num) for num in result])

    print('#{} {}'.format(tc, result))