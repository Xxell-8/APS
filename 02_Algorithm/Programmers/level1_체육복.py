# 1. 카운팅 정렬 활용
def count_tracksuit(n, lost, reserve):
    count = [1] * n

    for num in lost:
        count[num-1] -= 1
    for num in reserve:
        count[num-1] += 1

    for idx in range(n):
        if count[idx] == 0:
            if idx-1 >= 0 and count[idx-1] == 2:
                count[idx] += 1
                count[idx-1] -= 1
            elif idx+1 < n and count[idx+1] == 2:
                count[idx] += 1
                count[idx+1] -= 1

    answer = 0
    for idx in range(n):
        if count[idx] > 0:
            answer += 1
    return answer


# 2. in 활용
def find_tracksuit(n, lost, reserve):
    lost = [num for num in lost if num not in reserve]
    reserve = [num for num in reserve if num not in lost]

    answer = n - len(lost)
    for num in lost:
        if num - 1 in reserve:
            answer += 1
            reserve.remove(num-1)
        elif num + 1 in reserve:
            answer += 1
            reserve.remove(num+1)

    return answer


print(count_tracksuit(5, [2, 4], [1, 3, 5]))
print(count_tracksuit(5, [2, 4], [3]))
print(count_tracksuit(3, [3], [1]))
print(find_tracksuit(5, [2, 4], [1, 3, 5]))
print(find_tracksuit(5, [2, 4], [3]))
print(find_tracksuit(3, [3], [1]))