import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    cal = input()
    back = cal[0] + cal[2:] + '+'

    stack = []
    for i in range(n):
        if back[i] != '+':
            stack.append(int(back[i]))
        else:
            plus = stack.pop() + stack.pop()
            stack.append(plus)

    print('#{} {}'.format(tc, stack.pop()))