import sys
sys.stdin = open('input.txt')


def flatten(dump_limit, boxes):
    # 2-1. 정해진 덤프 횟수만큼 반복
    for _ in range(dump_limit):
        # 2-2. 가장 높은 곳과 가장 낮은 곳 계산
        max_idx = 0
        min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        # 2-3. 상자 하나 옮기기
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # 3-1. 차이가 0이나 1인지 확인
        max_idx = 0
        min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx
        diff = boxes[max_idx] - boxes[min_idx]

        # 3-2. 0이나 1이면 반복 중단 > return
        if diff == 0:
            return 0
        elif diff == 1:
            return 1

    # 4. 끝까지 돌면 마지막 차이 구하기
    max_idx = 0
    min_idx = 0
    for idx in range(len(boxes)):
        if boxes[idx] > boxes[max_idx]:
            max_idx = idx
        elif boxes[idx] < boxes[min_idx]:
            min_idx = idx
    return boxes[max_idx] - boxes[min_idx]


for tc in range(1, 11):
    # 1. 주어진 숫자를 받아오고
    dump_limit = int(input())
    boxes = list(map(int, input().split()))

    print('#{} {}'.format(tc, flatten(dump_limit, boxes)))