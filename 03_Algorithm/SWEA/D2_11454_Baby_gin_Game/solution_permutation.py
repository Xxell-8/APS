import sys
sys.stdin = open('input.txt')


def permutations(numbers):
    perms = []

    def recursive(done, remain):
        global cnt
        cnt += 1

        if remain == '':
            perms.append(done)
        else:
            for idx in range(len(remain)):
                rest = remain[:idx] + remain[idx+1:]
                recursive(done + remain[idx], rest)

    recursive('', numbers)
    return perms

T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    num = input()

    cnt = 0

    print(permutations('123'), cnt)