import sys
sys.stdin = open('input.txt')

# 2. 암호의 세부 규칙 저장
rules = {'0001101': 0, '0011001': 1, '0010011': 2,
         '0111101': 3, '0100011': 4, '0110001': 5,
         '0101111': 6, '0111011': 7, '0110111': 8,
         '0001011': 9}


# 3-1. 배열에서 필요한 부분만 추출하기
def scanner(info):
    # 3-1. 각 행을 돌면서 끝에서부터 탐색 > 암호가 무조건 1로 끝나기 때문에!
    for i in range(n):
        for j in range(m-1, -1, -1):
            if info[i][j] == '1':
                # 3-2. i, j가 추출할 부분의 끝
                code = info[i][j-55:j+1]
                return code


T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    n, m = map(int, input().split())
    info = [input() for _ in range(n)]

    # 4-1. info에서 필요한 부분만 추출
    code = scanner(info)
    # 4-2. code에서 7개씩 자르기
    decode = []
    for i in range(0, 56, 7):
        decode.append(rules[code[i:i+7]])

    # 5-1. 짝수 위치와 홀수 위치 계산
    even = 0
    odd = 0
    for idx in range(7):
        if idx % 2:
            even += decode[idx]
        else:
            odd += decode[idx] * 3

    # 5-2. 검증 코드 합산해서 정상적인 코드인지 확인
    verify = odd + even + decode[7]
    result = 0 if verify % 10 else sum(decode)

    print('#{} {}'.format(tc, result))
