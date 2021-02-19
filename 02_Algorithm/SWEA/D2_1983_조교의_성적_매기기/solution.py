import sys
sys.stdin = open('input.txt')

## index 활용 ##

T = int(input())
for tc in range(1, T+1):
    # 1. 필요한 input 받기
    n, target = map(int, input().split())

    # 2-1. 학생들의 총점을 담을 result 초기화
    result = []
    # 2-2. 학생 수(n)만큼 반복하며 총점 계산
    for _ in range(n):
        mid, fin, hw = map(int, input().split())
        score = mid*0.35 + fin*0.45 + hw*0.2
        result.append(score)

    # 3-1. target 학생의 등수를 담을 rank 초기화
    rank = 0
    # 3-2. 전체 성적을 순회하며 target 학생보다 점수가 높으면 +1
    ## index로 활용하기 때문에, 0등부터 시작
    for i in range(n):
        if result[i] > result[target-1]:
            rank += 1

    # 4-1. 10개의 평점을 담은 grades를 만들고
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # 4-2. 학생의 등수와 평점 비율을 계산
    final = rank // (n//10)
    answer = grades[final]

    print('#{} {}'.format(tc, answer))