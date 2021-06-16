import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))

    # 2-1. 화덕으로 사용할 fire 초기화
    fire = []
    # 2-2. 화덕 크기만큼 pizza 채우기
    for i in range(n):
        fire.append([pizza[i], i]) # 치즈와 피자 번호 저장

    # 3. 다음 추가할 피자는 n부터
    i = n
    # 4. 화덕에 피자 하나 남을 때까지
    while len(fire) != 1:
        # 5-1. 1번 위치 피자의 치즈 절반
        fire[0][0] //= 2

        # 5-2. 1번 위치 피자 치즈가 다 녹으면
        if not fire[0][0]:
            # 5-3. 해당 피자 빼고
            fire.pop(0)
            # 5-4. 다음 피자가 있으면 화덕에 추가
            if i < m:
                # 5-5. 한 바퀴 돌아야 치즈가 녹으니까 맨 뒤에 넣기
                fire.append([pizza[i], i])
                i += 1

        # 5-5. 치즈가 덜 녹았으면
        else:
            # 5-6. 다시 맨 뒤로
            fire.append(fire.pop(0))

    result = fire[0][1] + 1

    print('#{} {}'.format(tc, result))