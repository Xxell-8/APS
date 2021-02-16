import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    case = int(input())
    game = [list(map(int, input().split())) for _ in range(100)]

    # 1. 도착점을 찾는다
    for idx in range(100):
        if game[99][idx] == 2:
            row = idx
            break

    # 2. 도착점에서 출발점까지 거슬러 올라간다
    col = 98
    while col > 0:
        left = row - 1
        while 0 <= left < 100 and game[col][left] == 1:
            game[col][left] = 2
            row = left
            left = row - 1

        right = row + 1
        while 0 <= right < 100 and game[col][right] == 1:
            game[col][right] = 2
            row = right
            right = row + 1

        col -= 1

    print('#{} {}'.format(tc, row))
