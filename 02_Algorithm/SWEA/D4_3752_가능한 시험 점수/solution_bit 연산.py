import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    result = []

    for i in range(1 << n):
        score = 0
        for j in range(n):
            if i & (1 << j):
                score += scores[j]
        if score not in result:
            result.append(score)

    #print('#{} {}'.format(tc, result))

    print('#{} {}'.format(tc, len(result)))