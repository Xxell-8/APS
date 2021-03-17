import sys
sys.stdin = open('input.txt')


def solution(text):
    stack = []
    openers = '([{'
    closers = ')]}'
    for char in text:
        if char in openers:
            stack.append(char)

        if char in closers:
            # 1. stack이 비었을 경우
            if not stack:
                return 0
            else:
                # 2. pair가 안 맞을 경우
                if char == ')' and stack.pop() != '(':
                    return 0
                elif char == ']' and stack.pop() != '[':
                    return 0
                if char == '}' and stack.pop() != '{':
                    return 0

    # 3. 다 끝나고 stack에 뭐가 있을 경우
    else:
        if stack:
            return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    text = input()
    print('#{} {}'.format(tc, solution(text)))