import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. 필요한 변수를 생성
    max_len = 0
    words = []
    result = ''
    # 2-1. input 값을 받고, 받은 문자열의 최대 길이 구하기
    for _ in range(5):
        text = input()
        if len(text) > max_len:
            max_len = len(text)
        # 2-2. (문제 조건 활용) input의 최대 길이인 15만큼 # 채우기
        words.append(text.ljust(15, '#'))

    # 3-1. 필요한 범위를 순회
    for j in range(max_len):
        for i in range(5):
            # 3-2. #이 아니면 추가
            if words[i][j] != '#':
                result += words[i][j]

    print('#{} {}'.format(tc, result))