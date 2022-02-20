def solution(number, k):
    # 1-1. 큰 수를 담을 answer 변수 초기화
    answer = ''
    # 1-2. 최종 길이 length 계산
    length = len(number) - k

    # 2-1. 주어진 숫자를 하나씩 순회하면서
    for i in range(len(number)):
        # 2-2. 남은 삭제 횟수가 0이면 종료 
        if k == 0:
            answer += number[i:]
            break
        
        # 2-3. 최종 길이를 다 채우면 종료
        if len(answer) == length:
            break

        # 2-4. 0일 경우, 무조건 다른 수보다 작으니 삭제
        if number[i] == '0':
            k -= 1
            continue
        
        # 2-5. 9일 경우, 무조건 다른 수보다 크기 때문에 answer에 추가
        if number[i] == '9':
            answer += number[i]
            continue
        
        # 2-6. 아니라면 남은 수들과 비교
        for j in range(i+1, len(number)):
            if number[i] < number[j]:
                if len(answer) + len(number[j:]) >= length:
                    k -= 1
                    break
        else:
            answer += number[i]

    return answer


print(solution('1924', 2))
print(solution('1000', 1))
print(solution('1231234', 3))
print(solution('4177252841', 4))