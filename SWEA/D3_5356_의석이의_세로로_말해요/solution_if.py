import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. 필요한 변수 생성
    max_len = 0
    board = []
    result = ''

    # 2. input 값을 받고, 받은 문자열의 최대 길이 구하기
    for _ in range(5):
        word = input()
        if len(word) > max_len:
            max_len = len(word)
        board.append(word)

    # 3-1. max_len 만큼(열 기준) 반복
    for j in range(max_len):
        for i in range(5):
            # 3-2. 해당 문자열의 길이가 읽으려 하는 열보다 클 때만 추가
            if len(board[i]) > j:
                result += board[i][j]

    print('#{} {}'.format(tc, result))