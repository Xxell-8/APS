import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    neighbor = [-2, -1, 1, 2]
    result = 0

    idx = 2
    while idx < n-2:
        height = 0
        for nb in neighbor:
            if buildings[idx+nb] > height:
                height = buildings[idx+nb]

        if buildings[idx] > height:
            result += buildings[idx] - height
            idx += 3
        else:
            idx += 1


    print('#{} {}'.format(tc, result))
