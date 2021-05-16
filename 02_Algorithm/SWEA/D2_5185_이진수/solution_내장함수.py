import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, number = input().split()
    result = ''

    for char in number:
        result += '{:04b}'.format(int(char, 16))

    print('#{} {}'.format(tc, result))