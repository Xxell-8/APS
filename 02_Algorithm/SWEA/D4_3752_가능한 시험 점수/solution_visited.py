# KEY > bit 연산 비슷하게 구현하되, 연산 횟수 줄이기

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n = int(input())
    scores = list(map(int, input().split()))

    # 2-1. 가능한 최고 점수 계산
    max_score = sum(scores)
    # 2-2. 0점을 포함해서 visited 생성
    visited = [0] * (max_score + 1)
    # 2-3. 0점은 무조건 가능하니까 True 처리
    visited[0] = 1

    # 3-1. 문제의 배점들을 순회하면서
    for score in scores:
        # 3-2. visited 순회
        # 현재 문제의 배점을 더했을 때, 최고점수를 넘지 않는 선에서부터 시작
        # 끝에서부터 돌아야 현재 배점이 중복되서 계산되지 않음
        for i in range((max_score + 1) - score, -1, -1):
            # 3-3. 해당 점수가 가능하면, 거기서 새로운 배점을 더한 점수도 가능
            if visited[i]:
                visited[i + score] = 1

    print('#{} {}'.format(tc, sum(visited)))