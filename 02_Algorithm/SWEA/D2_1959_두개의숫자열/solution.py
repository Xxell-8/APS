import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. 주어진 숫자를 받아오고
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 2. 길이 비교를 위해 a은 짧은 리스트, b은 긴 리스트로 통일
    if n > m:
        n, m = m, n
        a, b = b, a

    # 3. result 변수 초기화
    result = 0
    # 4. 2개 리스트의 길이 차이(diff)만큼 반복
    for diff in range(m-n+1):
        total = 0
        # 5. diff를 활용해서 마주보는 위치 이동
        for idx in range(n):
            total += a[idx] * b[idx + diff]
        # 6. 최댓값 구하기
        if total > result:
            result = total

    print('#{} {}'.format(tc, result))