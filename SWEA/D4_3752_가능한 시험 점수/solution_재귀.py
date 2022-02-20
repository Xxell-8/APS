import sys
sys.stdin = open('input.txt')


def possible_score(idx, score):
    if idx == n:
        if score not in result:
            result.append(score)
        return

    possible_score(idx+1, score + scores[idx])
    possible_score(idx+1, score)



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    result = []

    possible_score(0, 0)

    print('#{} {}'.format(tc, len(result)))