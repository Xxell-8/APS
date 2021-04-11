def solution(word):
    # 1. stack 생성
    stack = []

    # 2. word를 순회하면서
    for char in word:
        # 3-1. 빈 stack이면 추가
        if not stack:
            stack.append(char)

        # 3-2. 아니면 비교
        else:
            # 3-3. 같은 철자면 지우고
            if stack[-1] == char:
                stack.pop()
            # 3-4. 다른 철자면 stack에 쌓기
            else:
                stack.append(char)

    return 0 if stack else 1

print(solution('cdcd'))
print(solution('baabaa'))