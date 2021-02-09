import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))

    bus = 0
    bus_move = 0
    result = 0
    while bus < n - k:
        for stop in range(bus + k, bus, -1):
            if stop in charger:
                bus_move = stop
                break

        if bus == bus_move:
            bus = n
            result = 0
        else:
            bus = bus_move
            result += 1

    print('#{} {}'.format(tc, result))