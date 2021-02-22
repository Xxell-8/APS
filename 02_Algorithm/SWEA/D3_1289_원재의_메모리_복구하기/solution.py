import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    memory = input()
    count = 0

    if memory[0] == '1':
        count += 1

    for idx in range(1, len(memory)):
        if memory[idx-1] != memory[idx]:
            count += 1

    print('#{} {}'.format(tc, count))