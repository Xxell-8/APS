import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    text = input()
    stack = []
    result = 1

    for char in text:
        if char in '{[(':
            stack.append(char)

        if char == '}':
            if not stack:
                result = 0
                break
            elif stack.pop() != '{':
                result = 0
                break
        elif char == ']':
            if not stack:
                result = 0
                break
            elif stack.pop() != '[':
                result = 0
                break
        elif char == ')':
            if not stack:
                result = 0
                break
            elif stack.pop() != '(':
                result = 0
                break
    else:
        if stack:
            result = 0

    print('#{} {}'.format(tc, result))