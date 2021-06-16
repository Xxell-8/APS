import sys
sys.stdin = open('input.txt')

# test case가 10000000개라서 제한시간 초과

def find_b(a):
    b = 1
    while True:
        if ((a * b) ** (1 / 2)) % 1 == 0:
            return b
        b += 1

T = int(input())
for tc in range(1, T + 1):
    a = int(input())

    print('#{} {}'.format(tc, find_b(a)))