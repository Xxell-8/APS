import sys
sys.stdin = open('input.txt')

# A와 B를 찾는 함수 생성
def find_ab(D, K):
    # 2-1. D를 기준으로 K를 만들기 위해 필요한 A, B의 계수 찾기
    cal = [(0, 0), (1, 0), (0, 1)]
    idx = 3
    # 2-2. DP 활용 - 어제와 그저께 떡의 갯수 더하기
    while idx <= D:
        cal.append((cal[idx - 2][0] + cal[idx - 1][0], cal[idx - 2][1] + cal[idx - 1][1]))
        idx += 1
    # 2-3. A, B의 계수 저장
    x, y = cal[D]

    # 3-1. A와 B에 들어갈 수 있는 숫자를 순회하며
    for a in range(K):
        for b in range(K):
            # 3-2. 조건에 맞는 A, B를 찾으면 return
            if x * a + y * b == K:
                return a, b

# 1. input 받기
D, K = map(int, input().split())

# 4. A, B 계산 후 출력
A, B = find_ab(D, K)
print(f'{A}\n{B}')