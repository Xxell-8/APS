import sys
sys.stdin = open('input.txt')


# KEY > 물병은 총 3개이며, 물의 전체 양은 변하지 않으므로 A,B가 가진 물의 양으로 계산
def bfs():
    # 5. 이전에 옮긴 적 있는 조합인지 확인 > 처음이면 q에 추가
    def pour(current_a, current_b):
        if (current_a, current_b) not in check:
            check.append((current_a, current_b))
            q.append((current_a, current_b))

    # 2-1. 가능한 A/B 병의 물의 양을 저장할 q 초기화
    q = [(0, 0)]
    # 2-2. 체크한 적 있는지 확인하는 check 변수 초기화
    check = [(0, 0)]
    # 2-3. C병에 담길 수 있는 물의 양을 기록할 answer 변수 초기화
    answer = []

    # 3-1. 가능한 A, B의 조합이 있으면
    while q:
        # 3-2. 현재 ABC가 가진 물의 양 wa, wb, wc 저장
        wa, wb = q.pop(0)
        wc = C - wa - wb

        # 3-3. A병이 비어 있으면 C병의 물의 양 answer에 저장
        if not wa:
            answer.append(wc)

        # 4. 옮길 수 있는 물의 양을 확인하고 옮겨보기
        if wa > 0:
            # A -> B
            water = min(wa, B-wb)
            pour(wa-water, wb+water)

            # A -> C
            water = min(wa, C-wc)
            pour(wa-water, wb)

        if wb > 0:
            # B -> A
            water = min(wb, A-wa)
            pour(wa+water, wb-water)

            # B -> C
            water = min(wb, C-wc)
            pour(wa, wb-water)

        if wc > 0:
            # C -> A
            water = min(wc, A-wa)
            pour(wa+water, wb)

            # C -> B
            water = min(wc, B-wb)
            pour(wa, wb+water)

    return answer


# 1. input 받기
A, B, C = map(int, input().split())

# 6. 탐색 후 결과 출력
result = ' '.join(map(str, sorted(bfs())))
print(result)
