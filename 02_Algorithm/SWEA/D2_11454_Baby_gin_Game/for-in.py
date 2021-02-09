import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    count = [0] * 10

    for _ in range(6):
        count[num % 10] += 1
        num //= 10

    baby_gin = 0
    for i in range(10):
        while count[i] >= 3:
            baby_gin += 1
            count[i] -= 3

        if i < 8:
            while count[i] and count[i+1] and count[i+2]:
                baby_gin += 1
                count[i] -= 1
                count[i+1] -= 1
                count [i+2] -= 1

    result = 1 if baby_gin == 2 else 0
    print('#{} {}'.format(tc, result))
