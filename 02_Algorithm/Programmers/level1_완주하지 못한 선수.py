from collections import Counter
# KEY > 완주하지 못한 선수는 단 1명


# 1. Dictionary 활용
def marathon_dict(participant, completion):
    runners = {}

    for name in participant:
        runners[name] = runners.get(name, 0) + 1

    for name in completion:
        runners[name] -= 1

    for key, val in runners.items():
        if val > 0:
            return key


# 2. sort 활용
def marathon_sort(participant, completion):
    participant.sort()
    completion.sort()

    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            return participant[idx]
    else:
        return participant[-1]


# 3. Counter 활용
def marathon_counter(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]


participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

print(marathon_dict(participant, completion))
print(marathon_sort(participant, completion))
print(marathon_counter(participant, completion))