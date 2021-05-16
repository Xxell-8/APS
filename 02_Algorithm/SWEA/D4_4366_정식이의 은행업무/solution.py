import sys
sys.stdin = open('input.txt')


def guess(binary, ternary):
    # 1. result 초기화
    result = []

    # 2-1. 2진수를 한 자리씩 돌면서
    for idx in range(len(binary)):
        for fix in ['0', '1']:
            # 2-2. 해당 자리의 숫자를 고치고
            if binary[idx] != fix:
                fix_num = binary[:idx] + fix + binary[idx+1:]
                # 2-3. 10진수로 변환해서 result에 추가
                decimal = int(fix_num, 2)
                result.append(decimal)

    # 3-1. 3진수도 같은 방식으로 10진수 변환
    for idx in range(len(ternary)):
        for fix in ['0', '1', '2']:
            if ternary[idx] != fix:
                fix_num = ternary[:idx] + fix + ternary[idx+1:]
                decimal = int(fix_num, 3)
                # 3-2. 위에서 고친 숫자들 중에 존재하면 추측할 수 있는 송금액
                if decimal in result:
                    return decimal


T = int(input())
for tc in range(1, T + 1):
    binary = input()
    ternary = input()

    print('#{} {}'.format(tc, guess(binary, ternary)))