import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    D, A, B, F = map(int, input().split())

    # 2. 기차가 충돌할 때까지 걸리는 시간 구하기
    time = D / (A+B)

    # 3. 그 시간 동안 파리가 날 수 있는 거리
    fly = time * F

    print('#{} {}'.format(tc, fly))