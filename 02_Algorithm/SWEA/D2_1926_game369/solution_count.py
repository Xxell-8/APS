N = 40
clap = ['3', '6', '9']

for num in range(1, N+1):
    turn = str(num)
    count = 0
    for char in turn:
        if char in clap:
            count += 1

    if count > 0:
        turn = '-' * count

    print(turn, end=' ')