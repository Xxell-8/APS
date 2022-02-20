import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    num = int(input())

    # 2-1. 카운팅 정렬에 활용할 count 초기화
    count = [0] * 10
    # 2-2. num 의 한 자릿수씩 빼서 counting
    for _ in range(6):
        count[num % 10] += 1
        num //= 10

    # 3. 결과값을 담을 Baby-gin 초기화
    baby_gin = 0

    # 4. count를 순회하며 Baby-gin 확인
    for i in range(10):
        # 5-1. 같은 숫자가 3개 이상이면 triplet!
        while count[i] >= 3:
            # 5-2. 결과값 +1, 해당 카드 3장 빼기
            baby_gin += 1
            count[i] -= 3

        # 6-1. run의 최대 시작점은 7
        if i < 8:
            # 6-2. 연이은 숫자 3개가 1개 이상이면 run!
            while count[i] and count[i+1] and count[i+2]:
                # 6-3. 결과값 +1, 각 숫자 카드 1장씩 빼기
                baby_gin += 1
                count[i] -= 1
                count[i+1] -= 1
                count [i+2] -= 1

    # 7. 카드는 총 6장이므로, baby_gin이 2이면 1
    result = 1 if baby_gin == 2 else 0
    print('#{} {}'.format(tc, result))
