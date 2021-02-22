# KEY > 지원할 수 있는 부서의 최댓값이기 때문에 신청한 예산이 큰 부서부터 빼기
def account(d, budget):
    d.sort()

    while sum(d) > budget:
        d.pop()
    return len(d)


print(account([1, 3, 2, 5, 4], 9))
print(account([2, 2, 3, 3], 10))