game = [
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 2]
]

# 1. 도착점을 찾는다
for idx in range(10):
    if game[9][idx] == 2:
        row = idx
        break

# 2. 도착점에서 출발점까지 거슬러 올라간다
col = 8
while col > 0:
    left = row - 1
    while 0 <= left < 10 and game[col][left] == 1:
        game[col][left] = 2
        row = left
        left = row - 1

    right = row + 1
    while 0 <= right < 10 and game[col][right] == 1:
        game[col][right] = 2
        row = right
        right = row + 1


    col -= 1

print(col, row)