import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(range(1, 13))
    n, k = map(int, input().split())
    result = 0

    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(arr[j])
        if len(subset) == n and sum(subset) == k:
            result += 1
    print('#{} {}'.format(tc, result))