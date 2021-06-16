import sys
sys.stdin = open('input.txt')


# 2. 순열 만드는 함수 생성 > 자리를 하나씩 정해주는 방식
def perms(numbers):
    visit = []

    def recursive(fixed, remain):
        # 2-1. 더이상 추가할 게 없으면 visit에 추가
        if not remain:
            visit.append([0] + fixed + [0])

        else:
            # 2-2. 남아있는 값에서 하나씩 고정시키면서 순열 생성
            for idx in range(len(remain)):
                rest = remain[:idx] + remain[idx+1:]
                recursive(fixed + [remain[idx]], rest)

    recursive([], numbers)
    return visit


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input을 받고
    n = int(input())
    battery = [list(map(int, input().split())) for _ in range(n)]

    # 1-2. 사무실 번호를 저장해서
    office = list(range(1, n))
    # 1-3. 가능한 방문 순서 찾기
    orders = perms(office)

    result = []
    # 3-1. 가능한 방문순서를 모두 확인하면서
    for order in orders:
        total = 0
        for idx in range(len(order) - 1):
            # 3-2. 배터리 사용량 계산
            total += battery[order[idx]][order[idx+1]]
        result.append(total)

    print('#{} {}'.format(tc, min(result)))