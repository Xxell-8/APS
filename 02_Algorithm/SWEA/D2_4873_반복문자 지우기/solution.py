import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    text = input()

    stack = []
    idx = 0
    while idx < len(text):
        if stack:
            if stack[-1] != text[idx]:
                stack.append(text[idx])
            else:
                stack.pop()
        else:
            stack.append(text[idx])
        idx += 1

    print('#{} {}'.format(tc, len(stack)))