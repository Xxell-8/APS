import sys
sys.stdin = open('input.txt')

# KEY1 > 회문은 가운데를 기준으로 양 옆이 똑같음
## A, BAB, CBABC or AA , BAAB, CBAABC

# KEY2 > 2개짜리 회문부터 (최대)100개짜리 회문까지 있는지 확인
## KEY1 활용) 3개짜리 회문은 있는데, 4개짜리는 없을 수도 있다! 5개짜리 회문까지 확인 필요


# 4. 회문 검사 함수 생성
def palindrome(check, board):
    # 4-1. 글자 판(board)에서 한 줄(word)씩 가져오고
    for word in board:
        # 4-2. word를 순회하면서
        for start in range(100-check+1):
            # 4-3. check를 기준으로 양 옆을 확인하면서 회문 판별
            # check 길이의 회문이 있으면 return check
            for count in range(check // 2):
                if word[start+count] != word[start+check-1-count]:
                    break
            else:
                return check
    return 0


for _ in range(1, 11):
    # 1-1. 주어진 input 받기
    tc = int(input())
    row = [input() for _ in range(100)]
    # 1-2. zip 활용해서 세로 기준 단어 만들기
    col = [''.join(abc) for abc in zip(*row)]

    # 2-1. result 기본 값은 1 (회문 최소 길이)
    result = 1
    # 2-2. 가로 줄부터 탐색
    for check in range(2, 101):
        # 2-4. 새로운 result 이후 "2번" 회문 검사를 실행했는데,
        ## result가 변경되지 않았다면 break
        if check > result + 2:
            break
        # 2-3. check(길이)만큼의 회문이 존재하고,
        # 그 값이 result 보다 크면 result 변경
        if result < palindrome(check, row):
            result = check

    # 3. 위와 같은 방식으로 세로 줄 탐색
    for check in range(result+1, 101):
        if check > result + 2:
            break
        if result < palindrome(check, col):
            result = check

    print('#{} {}'.format(tc, result))