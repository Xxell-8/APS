import sys
sys.stdin = open('input.txt')

T = int(input())
# 1. 외계 언어 list 만들기
mars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    # 2. 주어진 input을 받고
    no_use = input()
    mars_num = input().split()

    # 3-1. 카운팅 정렬을 위한 count 초기화
    count = [0] * 10
    # 3-2. idx를 활용해 mars_num에 대응하는 count +1
    for num in mars_num:
        idx = mars.index(num)
        count[idx] += 1

    # 4. index 순서대로 result에 추가
    result = []
    for i in range(10):
        result += [mars[i]] * count[i]

    result = ' '.join(result)
    print('#{}\n{}'.format(tc, result))
