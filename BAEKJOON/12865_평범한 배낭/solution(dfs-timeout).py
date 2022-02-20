import sys
sys.stdin = open('input.txt')


def set_bag(weight, value, idx):
    global answer

    # 2-1. 물건을 하나씩 순회해서 다 돌면 가치 확인
    if idx == n:
        if value > answer:
            answer = value
        return

    # 2-2. 새로운 물건을 넣을 수 있으면,
    if weight + things[idx][0] <= k:
        # 넣고 확인하고
        set_bag(weight + things[idx][0], value + things[idx][1], idx + 1)
        # 넣지 않고 확인하고
        set_bag(weight, value, idx + 1)

    # 2-3. 못 넣으면 그보다 무거운 물건은 넣을 수 없으니
    else:
        # 종료 조건 맞춰주기
        set_bag(weight, value, n)


# 1-1. input을 받고
n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]
# 1-2. 무게순으로 정렬
things.sort(key=lambda x: x[0])

answer = 0

set_bag(0, 0, 0)
print(answer)