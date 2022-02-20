import sys
sys.stdin = open('input.txt')

# 3. 2진수를 매칭할 패턴 저장
code_match = {
    '211': 0, '221': 1, '122': 2, '411': 3,
    '132': 4, '231': 5, '114': 6, '312': 7,
    '213': 8, '112': 9,
}


# 4. 암호 해독 함수 생성
def decode(nums):
    res = []
    deci_code = []

    # 4-1. 양 옆의 1을 기준으로 1, 0, 1의 개수 세기
    match = [0, 0, 0]
    for num in nums:
        if match[1] == 0 and match[2] == 0 and num == '1':
            match[0] += 1
        elif match[0] > 0 and match[2] == 0 and num == '0':
            match[1] += 1
        elif match[0] > 0 and match[1] > 0 and num == '1':
            match[2] += 1

        # 4-2. 1, 0, 1 패턴이 끝나면 매칭 시작
        if match[0] > 0 and match[1] > 0 and match[2] > 0 and num == '0':
            key = ''
            # 4-3. 암호 두께 확인 후 처리
            div = min(match)
            if div > 1:
                for idx in range(3):
                    match[idx] //= div
                    key += str(match[idx])
            else:
                key = ''.join([str(m) for m in match])

            # 4-4. 10진수 코드에 추가
            deci_code.append(code_match[key])
            # 4-5. match 초기화
            match = [0, 0, 0]

        # 4-6. 10진수가 8개 모이면 res에 담고 초기화
        if len(deci_code) == 8:
            res.append(deci_code)
            deci_code = []

    return res


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받기
    n, m = map(int, input().split())

    # 1-2. 암호코드 있는 부분 추출 > 1차 중복 제거(겹치는 코드가 남아있을 수 있음)
    info = set()
    for _ in range(n):
        data = input()[:m].strip('0')
        if data:
            info.add(data)

    result = []
    answer = 0
    for data in info:
        # 2-1. 16진수를 2진수로 변환 + 양 끝에 0 제거
        data = bin(int(data, 16))[2:].strip('0')
        # 2-2. 2진수 해독하기
        barcode = decode(data + '0')

        # 5-1. 해독된 암호 확인하면서
        for bar in barcode:
            # 5-2. 2차 중복 제거
            if bar not in result:
                result.append(bar)

                # 5-3. 유효한 데이터인지 확인
                even = 0
                odd = 0
                for idx in range(7):
                    if idx % 2:
                        even += bar[idx]
                    else:
                        odd += bar[idx] * 3

                validation = odd + even + bar[7]

                # 5-4. 유효하면 answer에 합산
                if not validation % 10:
                    answer += sum(bar)

    print('#{} {}'.format(tc, answer))










