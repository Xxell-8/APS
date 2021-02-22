def failure_late(N, stages):
    result = {}

    users = len(stages)
    step = 1
    while step <= N:
        if users != 0:
            stay = stages.count(step)
            result[step] = stay / users
        else:
            result[step] = 0

        step += 1
        users -= stay

    return sorted(result, key=lambda x: result[x], reverse=True)


print(failure_late(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(failure_late(4, [4, 4, 4, 4, 4]))