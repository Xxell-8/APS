import sys
sys.stdin = open('input.txt')


def charge(current, battery):
    global cnt

    # 2. 현재 위치에서 마지막 정류장까지 이동 가능하면 종료
    if current + battery >= last_stop:
        return

    max_step = 0
    for move in range(1, battery + 1):
        # 3-1. 현재에서 이동 가능한 위치
        idx = current + move
        # 3-2. 해당 위치에서 이동 가능
        possible = idx + chargers[idx]

        if possible >= max_step:
            max_step = possible
            next_stop, new_battery = idx, chargers[idx]

    cnt += 1
    charge(next_stop, new_battery)


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받기
    info = list(map(int, input().split()))
    # 1-2. 필요한 변수 생성
    last_stop = info[0]
    chargers = [0] + info[1:] + [0]
    cnt = 0

    charge(1, chargers[1])
    print('#{} {}'.format(tc, cnt))