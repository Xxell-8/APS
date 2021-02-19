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
    idx = 2
    while idx < n-2:
        # 4. 이웃한 건물의 최대 높이 계산
        height = 0
        for nb in neighbor:
            if buildings[idx+nb] > height:
                height = buildings[idx+nb]

        # 5-1. 해당 빌딩이 높으면
        if buildings[idx] > height:
            # 5-2. 차이 만큼 view 확보
            result += buildings[idx] - height
            # 5-3. 이웃 건물은 확보된 view가 없을테니 JUMP
            idx += 3
        # 5-4. 낮으면 다음 건물 확인
        else:
            idx += 1


    print('#{} {}'.format(tc, result))
