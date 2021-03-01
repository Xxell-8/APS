import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n, password = input().split()

    stack = []
    idx = 0
    while idx < int(n):
        if not stack:
            stack.append(password[idx])
        else:
            if stack[-1] != password[idx]:
                stack.append(password[idx])
            else:
                stack.pop()
        idx += 1

    result = ''.join(stack)

    print('#{} {}'.format(tc, result))