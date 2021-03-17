import sys
sys.stdin = open('input.txt')


def solution(n, m, puzzle):
	# 1. 회문 판별 함수 생성
    def palindrome(text):
        count = len(text) // 2
        while count:
            if text[count-1] != text[-count]:
                return 0
            else:
                count -= 1
        return 1

    # 2. puzzle 탐색
    for i in range(n):
        # 2-1. 가로 줄 회문 검사
        row_text = puzzle[i]
        for start in range(n - m + 1):
            result = row_text[start:start + m]
            if palindrome(result) == 1:
                return result

        # 2-2. 세로 줄 회문 검사
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