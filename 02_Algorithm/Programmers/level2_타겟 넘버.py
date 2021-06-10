def solution(numbers, target):

    def dfs(val, idx):
        nonlocal answer, target, n

        if idx == n:
            if val == target:
                answer += 1
                return
            else:
                return

        dfs(val + numbers[idx], idx + 1)
        dfs(val - numbers[idx], idx + 1)

    n = len(numbers)
    answer = 0
    dfs(0, 0)
    return answer



print(solution([1, 1, 1, 1, 1], 3))