import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. 주어진 값을 받고
    d, l, n = map(int, input().split())

    # 2. 총 데미지를 기록할 변수 damage 초기화
    damage = 0
    # 3. n의 다음 공격이 D(1+n*L%)이기 때문에, 0 ~ n-1 순회
    for i in range(n):
        damage += d*(1 + i * (l/100))

    print('#{} {}'.format(tc, int(damage)))