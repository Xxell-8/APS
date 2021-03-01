import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    work = input()
    stack = []
    total = 0

    for idx in range(len(work)):
        if work[idx] == '(':
            stack.append(work[idx])
        else:
            if work[idx-1] == '(':
                stack.pop()
                total += len(stack)
            else:
                stack.pop()
                total += 1

    print('#{} {}'.format(tc, total))