import sys
sys.stdin = open('input.txt')

# 1-1. input을 받고
cost = int(input())
# 1-2. 거스름돈 계산하기
change = 1000 - cost
# 1-3. 잔돈 종류 저장
coins = [500, 100, 50, 10, 5, 1]

# 2. 잔돈 개수를 저장할 answer 초기화
answer = 0
# 3-1. 잔돈을 큰 순서대로 순회하면서
for coin in coins:
    # 3-2. 잔돈 개수와 남은 돈 계산 반복
    cnt, rest = divmod(change, coin)
    answer += cnt
    change = rest

print(answer)