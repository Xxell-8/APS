import sys
sys.stdin = open('input.txt')


def password(queue):
    # 2-1. return 으로 while 종료
    while True:
        # 2-2. 1부터 5까지 반복
        for i in range(1, 6):
            # 3-1. 맨 앞에 숫자를 뽑아 i 만큼 빼고
            tmp = queue.pop(0) - i

            # 3-2. 0보다 작거나 같으면 프로그램 종료
            if tmp <= 0:
                queue.append(0)
                return queue
            # 3-3. 아니라면, 맨 뒤에 추가하고 작업 계속
            else:
                queue.append(tmp)


T = 10
for _ in range(1, T + 1):
    # 1. input 받기
    tc = int(input())
    queue = list(map(int, input().split()))

    result = ' '.join(map(str, password(queue)))
    print('#{} {}'.format(tc, result))