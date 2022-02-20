import sys
sys.stdin = open('input.txt')

# KEY > bit 활용

T = int(input())
for tc in range(1, T+1):
    # 1. 주어진 input을 받고
    arr = list(range(1, 13))
    n, k = map(int, input().split())

    # 2. result 변수 초기화
    result = 0

    # 3. bit 활용 > 000000000000 ~ 111111111111 순회
    for i in range(1 << 12):
        # 4. 부분 집합을 담을 subset 초기화
        subset = []
        # 5-1. arr의 인덱스를 순회
        for j in range(12):
            # 5-2. 해당 인덱스가 둘 다 1이면 부분 집합에 있는 경우
            if i & (1 << j):
                subset.append(arr[j])
        # 6. 각 부분집합이 조건을 만족하면 +1
        if len(subset) == n and sum(subset) == k:
            result += 1
    print('#{} {}'.format(tc, result))