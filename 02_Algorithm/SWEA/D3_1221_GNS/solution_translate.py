import sys
sys.stdin = open('input.txt')
# 번역) 외계어(str) -> 숫자(int) -> 오름차순 정렬 -> 외계어(str)


def mars_sort(mars_num):
    # 2. 외계 언어 list 생성
    mars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 3. 번역 함수 생성
    def translator(num):
        # 2-1. 숫자라면 외계 언어로 번역
        if type(num) == int:
            return mars[num]
        # 2-2. 문자(외계 언어)라면 index를 활용해서 숫자로 번역
        elif type(num) == str:
            for i in range(10):
                if num == mars[i]:
                    return i

    # 4-1. 외계어 -> 숫자
    earth = list(map(translator, mars_num))
    # 4-2. 정렬한 숫자 -> 외계어
    result = map(translator, sorted(earth))

    return ' '.join(result)


T = int(input())
for tc in range(1, T+1):
    # 1. input 받기
    n = int(input().split()[1])
    mars_num = input().split()

    print('#{}\n{}'.format(tc, mars_sort(mars_num)))