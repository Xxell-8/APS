import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    factors = [2, 3, 5, 7, 11]
    result = [0] * 5

    for idx in range(len(factors)):
        while n % factors[idx] == 0:
            n /= factors[idx]
            result[idx] += 1

    result = ' '.join([str(num) for num in result])
    print('#{} {}'.format(tc, result))