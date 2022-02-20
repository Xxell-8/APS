from collections import Counter
from itertools import combinations


def solution(orders, course):
    # 1. 결과를 담을 answer 변수 초기화
    answer = []
    # 2-1. 메뉴 조합 수를 순회하면서
    for cnt in course:
        # 2-2. 가능한 메뉴 조합을 담을 menus 초기화
        menus = []
        for order in orders:
            # 2-3. 각 주문에서 가능한 조합 계산하고
            menu = combinations(sorted(order), cnt)
            # 2-4. menus에 추가
            menus += menu

        # 3-1. 각 조합이 몇 개인지 확인
        menu_cnt = Counter(menus)

        # 3-2. 조합이 있으면
        if menu_cnt:
            # 3-3. 가장 많은 조합이 몇 개인지 구하고
            maximum = max(menu_cnt.values())
            # 3-4. 최댓값이 2 이상이면
            if maximum > 1:
                # 3-5. answer에 결과 담기
                answer += [''.join(menu) for menu in menu_cnt if menu_cnt[menu] == maximum]

    return sorted(answer)