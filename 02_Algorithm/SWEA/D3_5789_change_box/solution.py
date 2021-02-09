import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, q = map(int, input().split())
    boxes = [0] * n

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for idx in range(l-1, r):
            boxes[idx] = i

    result = ' '.join([str(num) for num in boxes])

    print('#{} {}'.format(tc, result))