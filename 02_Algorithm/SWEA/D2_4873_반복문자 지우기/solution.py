import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    text = input()

    stack = []
    idx = 0
    while idx < len(text):
        if stack:
            # 1. stack의 마지막 글자와 다르면 추가
            if stack[-1] != text[idx]:
                stack.append(text[idx])
            # 2. 같으면 stack의 마지막 글자 빼기
            else:
                stack.pop()
        # 3. stack이 비어있으면 무조건 추가
        else:
            stack.append(text[idx])
        idx += 1

    print('#{} {}'.format(tc, len(stack)))