from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    # 1. scoville을 최소힙으로 변환
    heapify(scoville)

    # 2. 가장 작은 수가 K보다 작으면 반복
    while scoville[0] < K:
        # 2-1. 길이가 2보다 작으면 합칠 수 없으니 -1 반환
        if len(scoville) < 2:
            return -1

        # 2-2. 가장 작은 두 음식을 뽑아 섞고 다시 push
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + b * 2)

        # 2-3. 섞은 횟수 증가
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))