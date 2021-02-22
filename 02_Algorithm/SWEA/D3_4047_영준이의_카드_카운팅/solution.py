import sys
sys.stdin = open('input.txt')

# 카드 판별 함수 생성
def card_count(cards):
    # 1-1. 카드 무늬 pattern / 무늬 별 카드 개수 count
    pattern = ['S', 'D', 'H', 'C']
    count = [13, 13, 13, 13]
    # 1-2. 이미 가지고 있는 카드 own_card
    own_card = []

    idx = 0
    while idx < len(cards):
        # 2. 현재 카드의 무늬를 찾고
        for i in range(4):
            if cards[idx] == pattern[i]:
                count_idx = i
                break

        # 3-1. 현재 카드를 보면서
        current = cards[idx:idx + 3]
        # 3-2. 이미 있으면 ERROR
        if current in own_card:
            return 'ERROR'
        # 3-3. 없으면 해당 무늬의 카운트 -1, 가지고 있는 카드에 현재 카드 추가
        else:
            own_card.append(current)
            count[count_idx] -= 1
        idx += 3

    return ' '.join([str(num) for num in count])

T = int(input())
for tc in range(1, T + 1):
    cards = input()
    print('#{} {}'.format(tc, card_count(cards)))