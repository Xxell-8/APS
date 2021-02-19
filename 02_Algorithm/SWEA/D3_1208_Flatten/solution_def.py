import sys
sys.stdin = open('input.txt')

def solution(dump_limit, boxes):
    for _ in range(dump_limit):
        max_idx = 0
        min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # 차이가 0이나 1인지 확인
        max_idx = 0
        min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx
        diff = boxes[max_idx] - boxes[min_idx]
        if diff == 0:
            return 0
        elif diff == 1:
            return 1

    # 마지막 차이 구하기
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

    print('#{} {}'.format(tc, solution(dump_limit, boxes)))