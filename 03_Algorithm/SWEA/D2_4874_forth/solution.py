import sys
sys.stdin = open('input.txt')


# 2. 후위연산 함수 생성
def back_cal(nums):
    # 2-1. 스택 생성
    stack = []

    for char in nums:
        # 2-2. 숫자면 스택에 추가
        if char.isdigit():
            stack.append(int(char))

        # 2-3. 숫자가 없으면 error
        elif char == '.':
            if len(stack) > 1:
                return 'error'
            return stack.pop()

        # 2-4. 연산 진행
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
    # 1. input 받기
    nums = input().split()

    print('#{} {}'.format(tc, back_cal(nums)))
