def collatz(n):
    result = 0
    for _ in range(500):
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

        result += 1

        if n == 1:
            break
    else:
        result = -1

    return result


print(collatz(6))
print(collatz(16))
print(collatz(626331))