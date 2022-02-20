def solution(n):
    answer = 0

    def set_queen(r, col, plus, minus):
        nonlocal answer

        if r == n:
            answer += 1

        for c in range(n):
            if c in col or (r+c) in plus or (r-c) in minus:
                continue

            set_queen(r+1, col + [c], plus + [r+c], minus + [r-c])

    set_queen(0, [], [], [])
    return answer