def change124(n):
    if n <= 3:
        return '124'[n-1]

    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]

print(change124(4))