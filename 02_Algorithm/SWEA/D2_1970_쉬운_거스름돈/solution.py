import sys
sys.stdin = open('input.txt')

# KEY > 큰 단위 우선

T = int(input())
# 1. S마켓에서 사용하는 돈의 종류를 내림차순으로 list에 담기
changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    # 2. input 받기
    money = int(input())

    # 3. 필요한 거스름돈의 개수를 기록할 result 초기화
    result = [0] * 8

    # 4. 돈의 종류만큼 반복하면서
    for idx in range(8):
        # 5-1. 만약 n이 해당하는 돈의 단위보다 크면
        if money // changes[idx]:
            # 5-2. 몫을 해당 result 값 위치에 넣고
            result[idx] = money // changes[idx]
            # 5-3. n은 나머지로 변경
            money %= changes[idx]

    result = ' '.join([str(num) for num in result])
    print('#{}\n{}'.format(tc, result))