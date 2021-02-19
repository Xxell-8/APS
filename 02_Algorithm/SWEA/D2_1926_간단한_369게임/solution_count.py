N = 40

# 1. 369를 담은 clap 생성
clap = ['3', '6', '9']

# 2. 1부터 N까지 수에서
for num in range(1, N+1):
    turn = str(num)
    count = 0

    # 3. 해당 턴의 숫자가 369 중 하나면 count +1
    for char in turn:
        if char in clap:
            count += 1

    # 4. 369가 있으면 박수로 변환
    if count > 0:
        turn = '-' * count

    print(turn, end=' ')