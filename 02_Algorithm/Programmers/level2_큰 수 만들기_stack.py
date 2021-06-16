def solution(number, k):
    # 1-1. 최종 길이 length 저장
    length = len(number) - k
    # 1-2. stack을 활용해서 숫자 비교
    stack = [number[0]]

    for num in number[1:]:
        # 1-3. stack에 숫자가 있고, 삭제횟수가 남아있을 때,
        # stack의 마지막 숫자와 현재 숫자를 비교 > 마지막 숫자가 더 작을 경우 삭제
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        # 1-4. 아니라면 stack에 추가
        stack.append(num)

    return ''.join(stack[:length])


print(solution('1924', 2))
print(solution('1000000', 3))
print(solution('1231234', 3))
print(solution('4177252841', 4))