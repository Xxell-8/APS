import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. 주어진 문자열을 받아오고
    a, b = input().split()
    # 2. 필요한 변수 설정/초기화
    la, lb = len(a), len(b)
    idx = 0
    result = 0

    # 3-1. a의 끝까지 순회하면서
    while idx < la:
        # 3-2. b의 길이만큼 a를 slicing > b와 같은지 확인
        if idx <= la-lb and a[idx:idx+lb] == b:
            # 3-3. 같으면 result +1, b의 길이만큼 idx 점프
            result += 1
            idx += lb
        # 3-3. 다르면 result +1, idx +1
        else:
            result += 1
            idx += 1

    print('#{} {}'.format(tc, result))