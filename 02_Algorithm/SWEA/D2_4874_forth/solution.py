import sys
sys.stdin = open('input.txt')


def back_cal(nums):
    stack = []

    for char in nums:
        if char.isdigit():
            stack.append(int(char))

        elif char == '.':
            if len(stack) > 1:
                return 'error'
            return stack.pop()

        else:
            if len(stack) < 2:
                return 'error'

            y = stack.pop()
            x = stack.pop()

            if char == '+':
                stack.append(x + y)
            elif char == '-':
                stack.append(x - y)
            elif char == '*':
                stack.append(x * y)
            elif char == '/':
                stack.append(x // y)


T = int(input())
for tc in range(1, T + 1):
    nums = input().split()

    print('#{} {}'.format(tc, back_cal(nums)))
