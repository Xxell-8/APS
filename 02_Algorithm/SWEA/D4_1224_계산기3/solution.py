import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    origin = input()
    stack = []

    # 1. 후위 계산식 만들기
    back = ''
    op = {'(': 0, '+': 1, '*': 2}
    for char in origin:
        if char.isdigit():
            back += char
        else:
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    back += stack.pop()
                stack.pop()
            else:
                while stack and op[stack[-1]] > op[char]:
                    back += stack.pop()
                stack.append(char)
    while stack:
        back += stack.pop()

    # 2. 후위 계산하기
    for char in back:
        if char.isdigit():
            stack.append(int(char))
        else:
            y = stack.pop()
            x = stack.pop()
            if char == '+':
                stack.append(x + y)
            elif char == '*':
                stack.append(x * y)

    print('#{} {}'.format(tc, stack[0]))