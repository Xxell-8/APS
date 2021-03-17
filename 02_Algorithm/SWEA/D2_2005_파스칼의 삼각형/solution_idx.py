import sys
sys.stdin = open('input.txt')


def pascal_triangle(n):
    result = [[] for _ in range(n)]

    # 1. 삼각형 모양대로 순회
    for i in range(n):
        for j in range(i + 1):
            # 2-1. 해당 줄의 양 끝이면 1 추가
            if j == 0 or j == i:
                result[i].append(1)

            # 2-2. 아니면, 왼쪽 위와 오른쪽 위 계산해서 추가
            else:
                last = result[i-1]
                num = last[j-1] + last[j]
                result[i].append(num)

    return [map(str, row) for row in result]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print('#{}'.format(tc))

    for n in pascal_triangle(n):
        print(' '.join(n))
