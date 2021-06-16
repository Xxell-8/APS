import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1. N과 Q 값을 각각 할당하고
    n, q = map(int, input().split())
    # 2. 현주의 상자들을 만들어준다
    boxes = [0] * n

    # 3. Q회 동안 반복하면서
    for i in range(1, q+1):
        # 4. 일정 범위(L, R)를 받고
        l, r = map(int, input().split())
        # 5. 해당 범위에 있는 박스의 이름을 i로 바꿔준다
        for idx in range(l-1, r):
            boxes[idx] = i

    # 6. 공백을 구분자로 하는 str으로 변환
    result = ' '.join([str(num) for num in boxes])

    print('#{} {}'.format(tc, result))