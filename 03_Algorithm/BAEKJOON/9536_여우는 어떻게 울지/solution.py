T = int(input())

for _ in range(T):
    # 1. 녹음을 받아 소리 구분
    origin = input().split()

    # 2-1. 다른 동물 소리를 담을 others 초기화
    others = []

    while True:
        # 2-2. 주어진 input을 받아
        known = input().split()

        # 2-3. 마지막 줄이면 break
        if len(known) > 3:
            break

        # 2-4. 아니면 울음소리만 저장
        others.append(known[2])

    # 3-1. 여우 울음소리 저장할 fox 초기화
    fox = ''
    # 3-2. 녹음된 울음 소리를 순회하면서
    for sound in origin:
        # 3-3. 다른 동물 소리가 아니면
        if sound not in others:
            # 3-4. 여우 소리에 포함 + 공백 주기
            fox += sound + ' '

    # 4. 출력 시, 우측 공백 제거
    print(fox.rstrip())