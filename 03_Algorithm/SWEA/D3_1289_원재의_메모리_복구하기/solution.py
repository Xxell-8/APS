import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    memory = input()

    # 2. bit 변경 횟수를 기록할 count 초기화
    count = 0

    # 3. 초기화 상태는 모든 bit 0
    # 3-1. 원래 메모리가 1로 시작하면 모든 bit 1 상태로 시작
    if memory[0] == '1':
        count += 1

    # 3-2. 원래 메모리의 bit를 보면서 직전 bit와 다를 때마다 count + 1
    for idx in range(1, len(memory)):
        if memory[idx-1] != memory[idx]:
            count += 1

    print('#{} {}'.format(tc, count))