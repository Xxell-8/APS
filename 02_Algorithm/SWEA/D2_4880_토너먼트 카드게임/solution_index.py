import sys
sys.stdin = open('input.txt')


def card_game(start, end):
    # 2-2. 한 명이 되면 해당 학생 번호 반환
    if start == end:
        return start

    # 2-1. 가운데를 기준으로 left, right 나누기 >> 재귀
    left = card_game(start, (start+end) // 2)
    right = card_game((start+end) // 2 + 1, end)

    # 3. 반환된 학생 번호를 받아 승자 확인
    if (cards[right] == 1 and cards[left] == 3
        or cards[right] == 2 and cards[left] == 1
        or cards[right] == 3 and cards[left] == 2):
        return right
    else:
        return left


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 1. 학생 번호와 인덱스 번호 맞춰주기
    cards = [0] + list(map(int, input().split()))

    print('#{} {}'.format(tc, card_game(1, n)))