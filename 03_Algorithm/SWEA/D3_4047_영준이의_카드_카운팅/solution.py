import sys
sys.stdin = open('input.txt')


# 카드 판별 함수 생성
def card_count(cards):
    # 2-1. 카드 무늬 patterns
    patterns = ['S', 'D', 'H', 'C']
    # 2-2. 각 무늬 별 카드 종류 labels
    labels = [13, 13, 13, 13]
    # 2-3. 내가 가진 카드 own_cards
    own_cards = []

    idx = 0
    while idx < len(cards):
        # 3-1. 현재 카드를 확인
        current = cards[idx:idx + 3]

        # 3-2. 이미 가지고 있는 카드라면, ERROR
        if current in own_cards:
            return 'ERROR'

        # 3-3. 새로운 카드면,
        else:
            # 3-4. 내 카드 목록에 추가
            own_cards.append(current)
            # 3-5. 카드 무늬 확인 후, 해당 무늬의 labels -1
            for i in range(4):
                if cards[idx] == patterns[i]:
                    pattern = i
                    break
            labels[pattern] -= 1

        # 4. 다음 카드로 이동
        idx += 3

    return ' '.join([str(num) for num in labels])

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    cards = input()
    print('#{} {}'.format(tc, card_count(cards)))