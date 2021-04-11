def solution(n):
    x, y = 1, 2
    if n == 1:
        return x
    if n == 2:
        return y

    for _ in range(n-2):
        x, y = y, (x+y) % 1000000007

    return y

print(solution(4))