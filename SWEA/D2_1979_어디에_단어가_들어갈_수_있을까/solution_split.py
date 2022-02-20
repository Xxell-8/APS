import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    n, k = map(int, input().split())
    row_puzzle = [''.join(input().split()) for _ in range(n)]

    # 2. zip 활용해서 세로 기준 퍼즐 만들기
    col_puzzle = [''.join(cell) for cell in zip(*row_puzzle)]

    # 3. 결과 값 result 초기화
    result = 0

    # 4. 각 행을 돌면서
    for idx in range(n):
        # 5-1. 0(막힌 칸) 기준으로 split > 공백과 1(빈 칸)만 남음
        row_blank = row_puzzle[idx].split('0')
        # 5-2. 분리된 칸의 길이가 k면 result +1
        for rb in row_blank:
            if len(rb) == k:
                result += 1
        col_blank = col_puzzle[idx].split('0')
        for cb in col_blank:
            if len(cb) == k:
                result += 1

    print('#{} {}'.format(tc, result))