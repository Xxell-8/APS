import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, target = map(int, input().split())

    result = []
    for i in range(1, n+1):
        mid, fin, hw = map(int, input().split())
        score = mid*0.35 + fin*0.45 + hw*0.2
        result.append(score)

    rank = 0
    for i in range(n):
        if result[i] > result[target-1]:
            rank += 1

    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    final = rank // (n//10)
    answer = grades[final]

    print('#{} {}'.format(tc, answer))