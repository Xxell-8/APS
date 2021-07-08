def solution(lottos, win_nums):
    # 1. 순위 정보 저장 > idx로 접근
    rank = [6, 6, 5, 4, 3, 2, 1]

    # 2-1. 낙서된 공의 갯수 구하기
    unknown = lottos.count(0)
    # 2-2. 당첨 번호와 겹치는 공의 갯수 구하기
    match = len(set(lottos) & set(win_nums))

    # 3. 낙서 공이 모두 당첨 번호일 경우와 모두 당첨 번호가 아닐 경우의 순위 반환
    return [rank[match + unknown], rank[match]]