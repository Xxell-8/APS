import sys
sys.stdin = open('input.txt')

# KEY > 도착점에서 거슬러 올라가기

for tc in range(1, 11):
    case = int(input())
    game = [list(map(int, input().split())) for _ in range(100)]

    # 1. 마지막 줄에서 도착점 idx 찾기
    for idx in range(100):
        if game[99][idx] == 2:
            row = idx
            break

    # 2. 마지막 줄에서는 이동하면 안 되니까 한 칸 위에서 시작
    col = 98
    # 3. 첫번째 줄에 올 때까지 반복
    # 좌우 확인 후 갈 수 있는 만큼 가고, 없으면 위로 가기
    # 지나온 길은 돌아갈 수 없으니까 값을 바꾸기
    while col > 0:
        # 4-1. 좌측 확인
        left = row - 1
        while 0 <= left < 100 and game[col][left] == 1:
            game[col][left] = 2
            row = left
            left = row - 1

        # 4-2. 우측 확인
        right = row + 1
        while 0 <= right < 100 and game[col][right] == 1:
            game[col][right] = 2
            row = right
            right = row + 1

        # 4-3. 좌우 확인 후에 위로 올라가기
        col -= 1

    print('#{} {}'.format(tc, row))
