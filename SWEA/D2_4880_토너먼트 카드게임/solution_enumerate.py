import sys
sys.stdin = open('input.txt')


def tournament(cards):
    # 5. 카드 비교 함수 생성
    def rcp(nums):
        if (nums[1][1] == 1 and nums[0][1] == 3
                or nums[1][1] == 2 and nums[0][1] == 1
                or nums[1][1] == 3 and nums[0][1] == 2):
            return nums[1]
        else:
            return nums[0]

    # 4-1. 만약 1명이면, 부전승
    if len(cards) == 1:
        return cards[0]
    # 4-2. 2명이면 카드 비교
    elif len(cards) == 2:
        return rcp(cards)

    # 2-1. 그룹을 나눌 기준점 계산
    center = (cards[0][0] + cards[-1][0]) // 2

    # 2-2. left, right 나누기
    left, right = [], []
    for c in cards:
        if c[0] <= center:
            left.append(c)
        else:
            right.append(c)

    # 3. 각 그룹이 2명 이하가 되도록 재귀
    winner_left = tournament(left)
    winner_right = tournament(right)

    return rcp([winner_left, winner_right])


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 1. 학생 번호 확인을 위해 번호(1번부터)를 함께 저장
    cards = list(enumerate(map(int, input().split()), 1))

    print('#{} {}'.format(tc, tournament(cards)[0]))