import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. 소인수분해할 숫자 N을 받고
    n = int(input())
    
    # 2. 인수로 쓸 숫자를 list에 담고
    factors = [2, 3, 5, 7, 11]
    # 3. abcde를 계산할 숫자를 result에 할당한다
    result = [0] * 5

    # 4. factors와 result에 접근하기 쉽도록 idx로 순회
    for idx in range(len(factors)):
        # 5. N이 각각의 인수로 나누어 떨어질 동안
        while n % factors[idx] == 0:
            # 6. n을 해당 인수로 나누고
            n /= factors[idx]
            # 7. 해당 result 위치에 1을 더한다
            result[idx] += 1

    # 8. result를 str으로 변환
    result = ' '.join([str(num) for num in result])
    print('#{} {}'.format(tc, result))