import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 1. input 받기
    n = int(input())
    buildings = list(map(int, input().split()))

    # 2-1. 결과 값을 담을 result 초기화
    result = 0
    # 2-2. 양 옆 2칸을 확인할 neighbor 생성
    neighbor = [-2, -1, 1, 2]

    # 3. 양 옆 2칸 빼고 순회
    for i in range(2, len(buildings)-2):
        # 4. 이웃한 건물의 최대 높이 계산
        height = 0
        for nb in neighbor:
            if buildings[i+nb] > height:
                height = buildings[i+nb]

        # 5-1. 이웃 높이보다 해당 빌딩이 높으면
        if buildings[i] > height:
            # 5-2. 차이만큼 view 확보
            view = buildings[i] - height
            result += view

    print('#{} {}'.format(tc, result))

