import sys
sys.stdin = open('input.txt')


# KEY > 선택한 자리에 퀸을 놓을 경우, 공격할 수 있는 칸의 규칙 저장하기
# 열 idx, 대각선(+), 대각선(-)을 저장
def set_queen(r, col, plus, minus):
    global result

    # 1. 끝까지 행을 순회하면 n개의 퀸을 놓은 것 > result + 1
    if r == n:
        result += 1
        return

    # 2-1. 해당 행(r)의 요소를 순회하면서
    for c in range(n):
        # 2-2. 공격 가능한 위치라면 continue
        if c in col or (r+c) in plus or (r-c) in minus:
            continue

        # 2-3. 공격 불가한 위치면 추가하고 다음 행 탐색
        set_queen(r + 1, col + [c], plus + [r+c], minus + [r-c])


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    result = 0

    set_queen(0, [], [], [])
    print('#{} {}'.format(tc, result))