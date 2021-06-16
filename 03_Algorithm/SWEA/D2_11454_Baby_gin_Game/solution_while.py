import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. input 받기
    cards = list(map(int, list(input())))

    # 2-1. 카운팅 정렬에 활용할 count 초기화
    count = [0] * 10

    # 2-2. 카드 한 장씩 뽑아 세기
    for card in cards:
        count[card] += 1

    # 3. 결과값을 담을 Baby-gin 초기화
    baby_gin = 0

    # 4. count를 순회하며 Baby-gin 확인
    idx = 0
    while idx < len(count):
        # 5-1. 같은 숫자가 3개 이상이면 triplet!
        if count[idx] >= 3:
            # 5-2. 결과값 +1, 해당 카드 3장 빼기
            baby_gin += 1
            count[idx] -= 3
            # 5-3. 같은 경우가 또 있을 수 있으니 continue (idx 변동 없음)
            continue

        # 6-1. run의 최대 시작점은 7
        if idx < 8:
            # 6-2. 연이은 숫자 3개가 1개 이상이면 run!
            if count[idx] and count[idx+1] and count[idx+2]:
                # 6-3. 결과값 +1, 각 숫자 카드 1장씩 빼기
                baby_gin += 1
                count[idx] -= 1
                count[idx+1] -= 1
                count[idx+2] -= 1
                continue

        idx += 1

    # 7. 카드는 총 6장이므로, baby_gin이 2이면 1
    result = 1 if baby_gin == 2 else 0
    print('#{} {}'.format(tc, result))
