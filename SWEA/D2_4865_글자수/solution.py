import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    str1 = list(set(input())) # 중복 제거
    str2 = input()

    # 2. 글자 개수를 셀 count 초기화
    count = [0] * len(str1)

    # 3. str2에 str1이 있으면 count +1
    for i in range(len(str1)):
        for char in str2:
            if str1[i] == char:
                count[i] += 1

    result = max(count)

    print('#{} {}'.format(tc, result))