import sys
sys.stdin = open('input.txt')

# 1. input 받고
n, k = map(int, input().split())
weight = [0]
value = [0]
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

# 2. 각 물건 행에 무게 별 열을 만들어 DP 수행 (초기값 0)
bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

for stuff in range(1, n+1):
    for level in range(1, k+1):
        # 3-1. 같은 무게 레벨에서 이전 물건의 가치 확인
        old = bag[stuff - 1][level]

        # 3-2. 현재 무게 레벨에 물건이 들어갈 수 있으면
        if level >= weight[stuff]:
            # 3-3. 새로 계산한 가치와 비교
            new = bag[stuff-1][level-weight[stuff]] + value[stuff]
            # 3-4. 새로운 가치 합산이 크면 갱신
            if new > old:
                bag[stuff][level] = new
            # 3-5. 아니면 이전 값 저장
            else:
                bag[stuff][level] = old

        # 3-6. 현재 무게 레벨에 해당 물건이 들어갈 수 없으면 이전 값 저장
        else:
            bag[stuff][level] = old

print(bag[n][k])