import sys
sys.stdin = open('input.txt')


# 2. 원숭이 팀 나누기
# KEY > 2^7 = 128이므로 최대 128명을 7일 안에 다른 팀으로 분리 가능
def divide(left, right, day):
    global team_info
    
    # 2-1. 종료 조건 생성
    if left >= right or day == 7:
        return
    
    # 2-2. 가운데 포인트 잡고
    mid = (left+right) // 2
    # 2-3. 왼쪽은 A, 오른쪽은 B로 나누기
    for monkey in range(left, right+1):
        if monkey <= mid:
            team_info[day][monkey] = 'A'
        else:
            team_info[day][monkey] = 'B'

    # 3. 다음 날은 같은 팀을 같은 방식으로 A/B 나누기
    divide(left, mid, day+1)
    divide(mid+1, right, day+1)


# 1-1. input 받기
N = int(input())
# 1-2. 팀 정보를 저장할 리스트 생성
team_info = [[0 for _ in range(N+1)] for _ in range(7)]

# 4. 팀 분할
divide(1, N, 0)

# 5. 최종 정보를 담을 result 초기화
result = []

# 6-1. 7일 동안의 팀 정보를 보며
for day in range(7):
    tmp = ''
    for monkey in range(1, N+1):
        # 6-2. 팀이 이미 배정되어 있으면 반영하고
        if team_info[day][monkey]:
            tmp += team_info[day][monkey]
        # 6-3. 없으면, 아무 팀이나 상관 없으므로 홀/짝으로 A/B 배분
        else:
            tmp += 'A' if monkey % 2 else 'B'
    result.append(tmp)

answer = '\n'.join(result)
print(answer)