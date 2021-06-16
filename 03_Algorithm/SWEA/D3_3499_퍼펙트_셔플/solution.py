import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())
    cards = input().split()

    # 2-1. 분기점 잡기 > n이 짝수면 똑같이, 홀수면 앞쪽이 한 장 더
    center = (n+1) // 2
    # 2-2. 결과값 담을 result 초기화
    result = []

    # 3-1. idx 0에서 시작
    idx = 0
    while n:
        # 3-2. result에 카드 추가
        result.append(cards[idx])

        # 3-3. result 길이가 홀수면 뒷쪽 카드 그룹 차례
        if len(result) % 2:
            idx += center
        # 3-4. 짝수면 앞쪽 카드 그룹 차례
        else:
            idx -= center - 1

        n -= 1

    print('#{} {}'.format(tc, ' '.join(result)))