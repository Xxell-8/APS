import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # 1. input 정렬해서 받기
    w = [0] + sorted(list(map(int, input().split())))
    t = [0] + sorted(list(map(int, input().split())))

    # 2. 필요한 변수 초기화
    container = truck = 0
    result = 0

    # 3-1. 컨테이너와 트럭이 남아 있는 동안 확인
    while w and t:
        # 3-2. 컨테이너가 더 크면 운반 불가 > 해당 컨테이너 교체
        if container > truck:
            container = w.pop()

        # 3-3. 운반 가능하면 컨테이너 무게 더하고, 다음 컨테이너/트럭으로 넘어가기
        else:
            result += container
            container = w.pop()
            truck = t.pop()

    print('#{} {}'.format(tc, result))