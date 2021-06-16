import sys
sys.stdin = open('input.txt')

# KEY: 쇠막대기를 자르거나 쇠막대기가 끝나는 횟수를 더한다!

T = int(input())
for tc in range(1, T + 1):
    # 1. 주어진 문자열을 받아오고
    work = input()
    # 2. 필요한 변수 초기화
    ## 작업 중인 iron의 개수 > iron
    ## 작업 후 최종 iron 개수 > result
    iron = 0
    result = 0

    # 3-1. 확인해야 할 괄호의 경우의 수는 총 3가지
    ## ① iron 시작점 '(' ② iron 끝점 ')' ③ 레이저 '()'
    # 3-2. 레이저로 자르거나 쇠막대기가 끝나면 result + 1
    for i in range(len(work)):
        # 4. 시작점이면 작업 중인 iron +1
        if work[i] == '(':
            iron += 1
        # 5-1. 끝점이면 작업 중인 iron -1
        else:
            iron -= 1
            # 5-2. 레이저라면 작업 중인 iron 만큼 result에 추가
            if work[i-1] == '(':
                result += iron
            # 5-3. 레이저가 아니면, iron이 끝났으니까 result +1
            else:
                result += 1

    print('#{} {}'.format(tc, result))