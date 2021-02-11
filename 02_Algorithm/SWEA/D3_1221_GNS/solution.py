import sys
sys.stdin = open('input.txt')

T = int(input())
mars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    count = [0] * 10
    n = int(input()[3:])
    mars_num = input().split()

    for num in mars_num:
        idx = mars.index(num)
        count[idx] += 1

    result = []
    for i in range(10):
        result += [mars[i]] * count[i]

    result = ' '.join(result)
    print('#{}\n{}'.format(tc, result))
