import sys
sys.stdin = open('input.txt')

# 1. target을 찾을 때까지 이진 검색을 반복한 횟수를 반환하는 함수 만들기


def search_game(l, r, target):
    count = 0
    # 1-1. 문제의 조건상 target은 무조건 존재
    ## 종료 조건 없이 찾으면 return
    while True:
        count += 1
        c = (l + r) // 2

        if c == target:
            return count
        elif c > target:
            r = c
        else:
            l = c


T = int(input())
for tc in range(1, T+1):
    p, a, b = map(int, input().split())

    A = search_game(1, p, a)
    B = search_game(1, p, b)

    if A > B:
        result = 'B'
    elif A < B:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(tc, result))


