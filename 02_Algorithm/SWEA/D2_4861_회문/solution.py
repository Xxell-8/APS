import sys
sys.stdin = open('input.txt')


def solution(n, m, puzzle):
    def palindrome(text):
        count = len(text) // 2
        while count:
            if text[count-1] != text[-count]:
                return 0
            else:
                count -= 1
        return 1

    # 가로 줄
    for i in range(n):
        row_text = puzzle[i]
        for start in range(n - m + 1):
            result = row_text[start:start + m]
            if palindrome(result) == 1:
                return result

        # 세로 줄
        col_text = ''
        for j in range(n):
            col_text += puzzle[j][i]
        for start in range(n - m + 1):
            result = col_text[start:start + m]
            if palindrome(result) == 1:
                return result


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    puzzle = [input() for _ in range(n)]

    print('#{} {}'.format(tc, solution(n, m, puzzle)))