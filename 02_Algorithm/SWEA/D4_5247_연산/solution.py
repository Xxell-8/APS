import sys
from collections import deque
sys.stdin = open('input.txt')


def cal():
    nums = deque([(n, 0)])
    visited = {}

    while nums:
        current, cnt = nums.popleft()

        if visited.get(current, 0):
            continue
        else:
            visited[current] = 1

        next = [current + 1, current - 1, current * 2, current - 10]
        cnt += 1
        for num in next:
            if num == m:
                return cnt

            if 0 < num < 10 ** 6:
                nums.append((num, cnt))


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    print('#{} {}'.format(tc, cal()))