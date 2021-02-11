import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    bus_lines = []
    for _ in range(n):
        a, b = map(int, input().split())
        bus_lines.append((a, b))

    p = int(input())
    stop = []
    for _ in range(p):
        c = int(input())
        stop.append(c)

    result = [0] * p
    for start, end in bus_lines:
        for idx in range(len(stop)):
            if stop[idx] in range(start, end+1):
                result[idx] += 1

    result = ' '.join([str(num) for num in result])

    print('#{} {}'.format(tc, result))