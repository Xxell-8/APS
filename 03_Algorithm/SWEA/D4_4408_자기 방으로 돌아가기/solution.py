import sys
sys.stdin = open('input.txt')

# KEY > 학생을 하나씩 빼지 말고 겹치는 구간을 구하자

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 1. 방이 총 400개 / 구간은 200개
    corridor = [0] * 201
    for _ in range(n):
        # 2-1. 방 번호 a, b를 받고
        a, b = map(int, input().split())
        # 2-2. a, b 오름차순
        if a > b:
            a, b = b, a
        # 3. a-b 이동 구간 구하기
        start = (a+1) // 2
        end = (b+1) // 2
        # 4. 복도 구간에 이동 경로 추가
        for idx in range(start, end+1):
            corridor[idx] += 1

    # 5. 겹치면 따로 가야 하니까 시간 추가
    # 즉, 가장 많이 겹친 수가 걸리는 시간이 됨
    print('#{} {}'.format(tc, max(corridor)))