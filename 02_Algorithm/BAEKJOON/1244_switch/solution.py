import sys
sys.stdin = open('input.txt')


# 1. 스위치 상태를 바꾸는 함수 생성
def change(num):
    if num == 0:
        return 1
    elif num == 1:
        return 0

# 2-1. 스위치의 개수 s_len, 각 스위치의 상태 switch 받기
s_len = int(input())
switch = list(map(int, input().split()))

# 2-2. 학생수 n, 각 학생의 성별 sex, 받은 번호 num 받기
n = int(input())
for tc in range(n):
    sex, num = map(int, input().split())

    # 3-1. 남학생이라면,
    if sex == 1:
        # 3-2. 받은 번호의 배수에 위치한 스위치 모두 변경
        for i in range(1, s_len//num+1):
            switch[num * i - 1] = change(switch[num*i - 1])

    # 4-1. 여학생이라면,
    elif sex == 2:
        # 4-2. 받은 번호를 중심으로 설정하고 상태 변경
        center = num - 1
        switch[center] = change(switch[center])

        # 4-3. center를 기준으로 양 옆이 같으면 상태 변경
        step = 1
        while step <= center and center + step < s_len:
            if switch[center - step] == switch[center + step]:
                switch[center - step] = switch[center + step] = change(switch[center + step])
            else:
                break
            step += 1

# 5. 스위치가 20개 넘으면, 한 줄에 20개씩 출력
if s_len > 20:
    for idx in range(s_len):
        if idx >= 20 and idx % 20 == 0:
            print()
        print(switch[idx], end= ' ')
else:
    print(' '.join([str(num) for num in switch]))