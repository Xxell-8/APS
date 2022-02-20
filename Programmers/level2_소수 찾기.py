def solution(numbers):
    # 2-1. 소수 판별 함수 생성
    def is_prime(num):
        # 2-2. 0~3의 경우, 계산 없이 T/F 반환
        if num < 2:
            return False

        if num == 2 or num == 3:
            return True

        # 2-3. 루트 num까지의 수로 나누며 소수 판별(에라토스테네스의 체 활용)
        k = int(num ** (1/2))
        for i in range(2, k + 1):
            if not num % i:
                return False
        return True

    # 3-1. DFS 탐색 - 주어진 카드로 만들 수 있는 숫자를 생성하는 함수 만들기
    def make_nums(idx, num):
        nonlocal result

        # 3-2. 카드 갯수만큼 탐색하면, 소수인지 판별 후 함수 종료
        if idx == N:
            if num:
                check = int(num)
                if check not in result and is_prime(check):
                    result.append(check)
            return

        # 3-3. 새로운 숫자가 들어갈 수 있는 경우의 수 모두 계산
        for i in range(len(num)+1):
            make_nums(idx+1, num[:i] + numbers[idx] + num[i:])
        # 3-4. 새로운 숫자가 들어가지 않는 경우 계산
        make_nums(idx+1, num)

    # 1-1. 주어진 카드 갯수를 구하고
    N = len(numbers)
    # 1-2. 만들 수 있는 소수를 저장할 result 초기화
    result = []

    # 4-1. 숫자를 만들어 소수 판별
    make_nums(0, '')
    # 4-2. 가능한 소수의 갯수 return
    return len(result)

print(solution('17'))