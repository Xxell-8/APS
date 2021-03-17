import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    n = int(input())
    cards = list(map(int, input()))

    # 2. 숫자 카드 분리하기
    count = [0] * 10
    for num in cards:
        count[num] += 1

    # 3. 카드 번호와 개수를 기록할 변수 초기화
    card_num = 0
    card_count = 0

    # 4-1. idx가 카드 번호, count[idx]가 카드 개수
    for idx in range(10):
        # 4-2. 개수가 같으면 큰 숫자 카드를 달라고 했으니까
        # 같을 경우에도 card를 교체
        if count[idx] >= card_count:
            card_num = idx
            card_count = count[idx]

    print('#{} {} {}'.format(tc, card_num, card_count))