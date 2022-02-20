import sys
sys.stdin = open('input.txt')

# 6차 시도만에 성공
# KEY1 > 미리 소수를 구하고 시작하기
# KEY2 > tc가 천만 개이기 때문에 결과값 모아서 한 번에 출력하기

# 필요한 소수 구하기
# 1-1. 2를 기본 값으로 두고, 짝수는 제외
prime = [2]
# 1-2. A의 범위가 10 ** 7 이므로 범위의 반만 구함 (그 이상은 짝수 제곱이 될 수 없음)
for num in range(3, int(10 ** 3.5), 2):
    # 1-3. 소수 집함에 있는 수로 나눠지면 제외
    for p in prime:
        if not num % p:
            break
    else:
         prime.append(num)


# b의 최솟값을 찾는 함수 생성
def find_b(a):
    # 2-1. b의 기본값은 1
    b = 1
    # 2-2. a가 거듭제곱수이면 1을 반환
    if not a ** (1/2) % 1:
        return b

    else:
        # 2-3. 소수를 순회하면서
        for num in prime:
            tmp = 0
            # 2-4. a가 해당 숫자로 나누어지면,
            while not a % num:
                # 2-5. a를 몫으로 변경, tmp + 1
                a //= num
                tmp += 1

            # 2-6. tmp가 홀수이면 해당 숫자를 b에 곱해주기
            if tmp % 2:
                b *= num

            # 2-7. a가 1이 되거나 검사하는 소수가 a보다 커지면 중단
            if a == 1 or num > a:
                break
        # 2-8. a가 1보다 크면 b에 a 곱하기
        if a > 1:
            b *= a
    return b

result = []
T = int(input())
for tc in range(1, T + 1):
    a = int(input())
    # 3. 케이스마다 print를 하면 시간이 오래 걸려서 result에 추가하고 한 번에 print
    result.append('#{} {}'.format(tc, find_b(a)))

for answer in result:
    print(answer)