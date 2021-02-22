## 회문 판별 알고리즘 비교 ##


# 1. manacher algorithm
def manacher(s):
    s = '#' + '#'.join(s) + '#'
    N = len(s)
    count = [0] * N

    # r: 현재 확인 완료한 회문의 가장 먼 우측 idx
    # p: 현재까지 확인한 가장 긴 회문의 중심 idx

    r = p = 0
    for idx in range(1, N-1):
        if idx <= r:
            m_idx = 2 * p - idx

            # r 까지 확실한 부분만 갱신
            if count[m_idx] > r - idx:
                count[idx] = r - idx
            else:
                count[idx] = count[m_idx]


        # idx - count[idx] -> idx 기준 지금까지 확인한 회문 좌측 끝
        # idx + count[idx] -> idx 기준 지금까지 확인한 회문 우측 끝
        while idx - count[idx] -1 >= 0 and idx + count[idx] +1 < N and s[idx - count[idx] -1] == s[idx + count[idx] +1]:
            count[idx] += 1

        if r < idx + count[idx]:
            r = idx + count[idx]
            p = idx

    return max(count)


# 2. SWEA_1216_cell
def pal_cell(s):
    n = len(s)

    result = 1
    for length in range(2, n+1):
        if length > result + 2:
            break

        for l in range(n - length + 1):
            for r in range(length // 2):
                if s[l + r] != s[l + length - 1 - r]:
                    break
            else:
                len_pal = length
                break

        else:
            len_pal = 0

        if result < len_pal:
            result = len_pal

    return result

import sys
from datetime import datetime
sys.stdin = open('test.txt')

def solution(s):
    n = len(s)

    result = 1
    for length in range(2, n + 1):
        if length > result + 2:
            break

        for l in range(n - length + 1):
            for r in range(length // 2):
                if s[l + r] != s[l + length - 1 - r]:
                    break
            else:
                len_pal = length
                break

        else:
            len_pal = 0

        if result < len_pal:
            result = len_pal

    return result

T = int(input())
for tc in range(1, T+1):
    start = datetime.now()
    solution(input())
    end = datetime.now()
    print('#{} {}'.format(10 * 10**tc, end-start))