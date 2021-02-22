# KEY > 삼진법(0, 1, 2)과 124의 나라(1, 2, 4)의 방식이 유사
def change124(n):
    if n <= 3:
        return '124'[n-1]

    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]

print(change124(4))