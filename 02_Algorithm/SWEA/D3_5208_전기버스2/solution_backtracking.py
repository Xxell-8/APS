import sys
sys.stdin = open('input.txt')

def get_minimum_change(current, energy, change):
    global result

    if result <= change or energy < 0:
        return

    if current == n-1:
        result = change
        return

    get_minimum_change(current + 1, chargers[current] - 1, change + 1)
    get_minimum_change(current + 1, energy - 1, change)


T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    info = list(map(int, input().split()))
    n = info[0]
    chargers = info[1:]

    result = n
    get_minimum_change(1, chargers[0] - 1, 0)

    print('#{} {}'.format(tc, result))