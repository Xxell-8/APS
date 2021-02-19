import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. 주어진 input 값을 받고
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')

    # 2. submit에 없는 학생 번호를 출력
    for num in range(1, n+1):
        if not num in submit:
            print(num, end=' ')
    print()
