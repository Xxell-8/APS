import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    origin = input()
    stack = []

    # 1. 후위 계산식으로 변환
    back = ''
    op = {'+': 1, '*': 2}
    for idx in range(n):
        if origin[idx].isdigit():
            back += origin[idx]
        else:
            if not stack:
                stack.append(origin[idx])
            else:
                while stack and op[stack[-1]] > op[origin[idx]]:
                    back += stack.pop()
                stack.append(origin[idx])
    while stack:
        back += stack.pop()

    # 2. 후위 계산식 계산
    for char in back:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            y = stack.pop()
            x = stack.pop()
            stack.append(x+y)
        elif char == '*':
            y = stack.pop()
            x = stack.pop()
            stack.append(x*y)

    print('#{} {}'.format(tc, stack[0]))