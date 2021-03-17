import sys
sys.stdin = open('input.txt')


def perm(idx, sub_sum):
    global answer

    if sub_sum > n:
        return

    if idx == 3:
        if sub_sum == n:
            cnt = 0

            start1 = select[0]
            start2 = start1 + select[1]

            for i in flag[:start1]:
                for j in i:
                    if j != 'W':
                        cnt += 1

            for i in flag[start1:start2]:
                for j in i:
                    if j != 'B':
                        cnt += 1
            for i in flag[start2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            if answer > cnt:
                answer = cnt
        return

    for i in range(1, n-1):
        select[idx] = i
        perm(idx + 1, sub_sum + i)


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]

    select = [0, 0, 0]
    answer = 9999999999999

    perm(0, 0)

    print('#{} {}'.format(tc, answer))