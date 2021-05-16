import sys
sys.stdin = open('input.txt')

hexa = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def binary(num):
    bit = ''
    for _ in range(4):
        q, r = divmod(num, 2)
        bit = str(r) + bit
        num = q

    return bit


T = int(input())
for tc in range(1, T + 1):
    n, number = input().split()
    result = ''

    for char in number:
        result += binary(hexa[char])

    print('#{} {}'.format(tc, result))