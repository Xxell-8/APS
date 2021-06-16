def math_exam(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    results = [0, 0, 0]
    for idx in range(len(answers)):
        if answers[idx] == first[idx % len(first)]:
            results[0] += 1
        if answers[idx] == second[idx % len(second)]:
            results[1] += 1
        if answers[idx] == third[idx % len(third)]:
            results[2] += 1

    answer = []
    for idx in range(len(results)):
        if results[idx] == max(results):
            answer.append(idx+1)

    return answer

print(math_exam([1, 2, 3, 4, 5]))
print(math_exam([1, 3, 2, 4, 2]))
