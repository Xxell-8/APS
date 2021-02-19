def snail_num(n):
    snail = []
    for i in range(1, n+1):
        snail.append([0] * i)

    num = 0
    step = 1
    col, row = -1, 0

    while n > 0:

        for _ in range(n):
            col += step
            num += 1
            snail[col][row] = num
        n -= 1

        for _ in range(n):
            row += step
            num += 1
            snail[col][row] = num
        n -= 1

        for _ in range(n):
            col -= step
            row -= step
            num += 1
            snail[col][row] = num
        n -= 1

    result = []
    for row in snail:
        for num in row:
            result.append(num)

    return result

print(snail_num(4))
print(snail_num(5))
print(snail_num(6))