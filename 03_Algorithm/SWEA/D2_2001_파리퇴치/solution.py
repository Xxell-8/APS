import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. input 받기
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]

    # 2. 결과 값 result 초기화
    result = 0

    # 3. (n-m) * (n-m)까지만 접근
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 4-1. 해당 영역에서 파리채로 잡을 수 있는 파리 수 total 초기화
            total = 0
            # 4-2. 파리채 크기만큼 접근
            for mi in range(m):
                for mj in range(m):
                    total += flies[i + mi][j + mj]
            # 5. 최댓값 구하기
            if total > result:
                result = total
    print('#{} {}'.format(tc, result))
