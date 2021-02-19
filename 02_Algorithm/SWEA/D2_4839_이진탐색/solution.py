import sys
sys.stdin = open('input.txt')


# 1. target을 찾을 때까지 이진 검색을 반복한 횟수를 반환하는 함수 생성
def search_game(l, r, target):
    count = 0
    # 1-1. 문제의 조건상 target은 무조건 존재하므로 종료 조건 없이 찾으면 return
    while True:
        count += 1
        # 1-2. 가운데 지점을 찾고
        c = (l + r) // 2

        # 1-3. 같으면 종료
        if c == target:
            return count
        # 1-4. target이 작으면 우측을 버리고
        elif c > target:
            r = c
        # 1-5. target이 크면 좌측을 버리기
        else:
            l = c


T = int(input())
for tc in range(1, T+1):
    # 2. input을 받고
    p, a, b = map(int, input().split())

    # 3. 이진 검색 횟수를 A, B에 할당
    A = search_game(1, p, a)
    B = search_game(1, p, b)

    # 4. 더 작은 팀이 승리
    if A > B:
        result = 'B'
    elif A < B:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(tc, result))


