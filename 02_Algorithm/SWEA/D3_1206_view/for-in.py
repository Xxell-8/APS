import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    neighbor = [-2, -1, 1, 2]
    result = 0

    for i in range(2, len(buildings)-2):
        height = 0
        for nb in neighbor:
            if buildings[i+nb] > height:
                height = buildings[i+nb]

        if buildings[i] > height:
            view = buildings[i] - height
            result += view

    print('#{} {}'.format(tc, result))

