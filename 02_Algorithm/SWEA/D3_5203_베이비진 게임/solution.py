import sys
sys.stdin = open('input.txt')


# 3. babygin 검사
def is_babygin(count):
    for i in range(10):
        # 3-1. triplet인지 확인
        if count[i] >= 3:
            return True

        # 3-2. run인지 확인
        if i < 8:
            while count[i] and count[i+1] and count[i+2]:
                return True

    return False


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받고
    cards = list(map(int, input().split()))

    # 1-2. 각 플레이어의 카드 현황판 생성
    player1 = [0] * 10
    player2 = [0] * 10

    # 1-3. result 초기화
    result = 0

    # 2. 12장의 카드를 배분하면서 3장 이상 갖기 시작하면 매번 babygin 검사
    for idx in range(12):
        if not idx % 2:
            player1[cards[idx]] += 1
            if idx >= 4 and is_babygin(player1):
                    result = 1
                    break
        else:
            player2[cards[idx]] += 1
            if idx >= 5 and is_babygin(player2):
                    result = 2
                    break

    print('#{} {}'.format(tc, result))