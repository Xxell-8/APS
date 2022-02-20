# 1. 1부터 n 사이의 정수를 모두 확인
def count_prime_number(n):
    answer = 0
    for num in range(2, n+1):
        cnt = 0
        for divisor in range(2, num):
            if num % divisor == 0:
                cnt += 1
        if cnt == 0:
            answer += 1
    return answer


# 2. 에라토스테네스의 체 활용
# n의 크기가 커질수록 효율적인 방식
def eratosthenes(n):
    # 2-1. 차집합 활용을 위해 집합(set) 활용
    prime = set(range(2, n+1))

    # 2-2. n까지의 숫자(num)를 순회하면서
    for num in range(2, n+1):
        # 2-3. 만약 num이 prime에 있으면,
        # num의 2배수부터 지우는데, 최댓값 // 2보다 커지는 순간 지울 게 없어짐
        if num > max(prime)//2:
            break
        # 2-4. num이 prime에 있으면
        if num in prime:
            # 2-5. num을 제외한 num의 배수 전체를 prime에서 빼기
            prime -= set(range(2*num, n+1, num))
    return len(prime)


print(count_prime_number(1000))
print(count_prime_number(45))
print(count_prime_number(5))

print(eratosthenes(1000))
print(eratosthenes(10000))
print(eratosthenes(5))