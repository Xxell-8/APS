import sys
sys.stdin = open('input.txt')

## KEY > 달팽이 규칙 찾기 ##
'''
n = 3일 때,
1차 이동 > 오른쪽(+1)으로 3번 >> n
2차 이동 > 아래(+1)로 2번 >> n-1
3차 이동 > 왼쪽(-1)으로 2번 >> n-1
4차 이동 > 위(-1)로 1번 >> n-2
5차 이동 > 오른쪽(+1)으로 1번 >> n-2
'''

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 1. n * n 배열 만들기
    snail = [[0 for _ in range(n)] for _ in range(n)]

    # 2. 기초 세팅
    num = 1
    col, row = 0, -1
    step = 1

    # 3. n이 0이 될 때까지 반복
    while n > 0:
        for _ in range(n):
            row += step
            snail[col][row] = num
            num += 1
        n -= 1

        for _ in range(n):
            col += step
            snail[col][row] = num
            num += 1
        step *= -1

    print('#{}'.format(tc))
    for num in snail:
        print(*num)
