import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, l = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    # 2. result 초기화
    result = 0

    # 3. info 부분집합 구하기
    for i in range(1 << n):
        t = k = 0
        for j in range(n):
            if i & (1 << j):
                t += info[j][0]
                k += info[j][1]
                if k > l:
                    break

        # 4. 최댓값 구하기
        if k <= l and t > result:
            result = t

    print('#{} {}'.format(tc, result))