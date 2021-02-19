import sys
sys.stdin = open('input.txt')


def solution(string):
    lasers = []
    sticks = []

    for idx in range(len(string)):
        if string[idx] == '(':
            if string[idx+1] == ')':
                lasers.append((idx, idx+1))
            else:
                n = 0
                for j in range(idx, len(string)):
                    if string[j] == '(':
                        n += 1
                    else:
                        n -= 1
                    if n == 0:
                        sticks.append((idx, j))
                        break

    result = len(sticks)

    for sl, sr in sticks:
        for ll, lr in lasers:
            if sl < ll and sr > lr:
                result += 1
    return result



T = int(input())
for tc in range(1, T + 1):
    print('#{} {}'.format(tc, solution(input())))