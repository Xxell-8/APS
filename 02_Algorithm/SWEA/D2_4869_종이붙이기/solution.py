import sys
sys.stdin = open('input.txt')


def paper_memo(n):
    if n >= len(memo):
        memo.append(paper_memo(n - 1) + (2 * paper_memo(n - 2)))
    return memo[n]


memo = [0, 1, 3]

T = int(input())
for tc in range(1, T + 1):
    width = int(input()) // 10

    print('#{} {}'.format(tc, paper_memo(width)))


# 재귀 / Memoization / DP
def paper_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    return paper_recursion(n-1) + (paper_recursion(n-2) * 2)


memo = [0, 1, 3]
def paper_memo(n):
    if n >= len(memo):
        memo.append(paper_memo(n - 1) + (2 * paper_memo(n - 2)))
    return memo[n]


def paper_dp(n):
    paper = [0, 1, 3]

    for i in range(3, n+1):
        paper.append(paper_dp(n - 1) + (2 * paper_dp(n - 2)))
    return paper[n]