import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 1. (n-m) * (n-m)까지만 접근
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            # 2. 파리채 크기만큼 계산
            for r in range(m):
                for d in range(m):
                    col = i + r
                    row = j + d
                    total += flies[col][row]
            # 3. 최댓값 구하기
            if total > result:
                result = total
    print('#{} {}'.format(tc, result))
