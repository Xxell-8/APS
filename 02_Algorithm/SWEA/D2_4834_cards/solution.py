import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = int(input())

    count = [0] * 10
    for _ in range(n):
        count[nums % 10] += 1
        nums //= 10

    card_num = 0
    card_count = 0
    for idx in range(len(count)):
        if count[idx] >= card_count:
            card_num = idx
            card_count = count[idx]

    print('#{} {} {}'.format(tc, card_num, card_count))