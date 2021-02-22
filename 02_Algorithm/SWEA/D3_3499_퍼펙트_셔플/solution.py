import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cards = input().split()
    center = (n+1)//2

    idx = 0
    result = []
    while n:
        result.append(cards[idx])

        if len(result) % 2:
            idx += center
        else:
            idx -= center - 1

        n -= 1

    print('#{} {}'.format(tc, ' '.join(result)))