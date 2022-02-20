def fibonacci(n):
    fibo = [0, 1]

    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo[n] % 1234567


print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
