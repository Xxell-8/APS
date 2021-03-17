import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    # 1. input 받기
    n, password = input().split()

    # 2-1. 활용할 stack 생성
    stack = []

    # 2-2. n 만큼 반복
    idx = 0
    while idx < int(n):
        # 3-1. stack이 비어있으면 무조건 숫자를 넣고
        if not stack:
            stack.append(password[idx])

        # 3-2. 아니면, stack 마지막 요소와 현재 숫자 비교
        else:
            # 3-3. 다르면 stack에 추가
            if stack[-1] != password[idx]:
                stack.append(password[idx])
            # 3-4. 같으면 둘 다 버리기
            else:
                stack.pop()
        idx += 1

    result = ''.join(stack)
    print('#{} {}'.format(tc, result))