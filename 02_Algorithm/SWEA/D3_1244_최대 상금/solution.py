import sys
sys.stdin = open('input.txt')


def change(nums, idx, cnt):
    # 2-1. 정해진 횟수만큼 교환한 경우
    if cnt == limit:
        # result에 추가하고 return
        result.append(int(''.join(nums)))
        return

    # 2-2. 숫자판 처음부터 끝까지 최댓값으로 swap이 끝난 경우
    elif idx == n:
        # 남은 횟수가 홀수이고, 중복되는 숫자가 없으면 마지막 두 자리 바꿔주기
        if (limit - cnt) % 2 and len(set(nums)) == n:
            nums[n-1], nums[n-2] = nums[n-2], nums[n-1]
        # result에 추가하고 return
        result.append(int(''.join(nums)))
        return

    # 3-1. 현재 교환할 위치의 값 current
    current = nums[idx]
    # 3-2. 교환할 수 있는 값 중 최댓값 max_num
    max_num = max(nums[idx:])

    # 4-1. 최댓값이 current라면,
    if max_num == current:
        # 현재 숫자판 그대로 넣고, 다음 자릿수로 넘어가기
        change(nums[:], idx+1, cnt)

    # 4-3. 아니면 교환 필요
    else:
        # 현재 자릿수에 최댓값을 넣고
        nums[idx] = max_num
        # 최댓값 위치를 찾아 숫자판 바꿔주기
        for swap in range(idx+1, n):
            if nums[swap] == max_num:
                change(nums[:swap] + [current] + nums[swap+1:], idx+1, cnt+1)


T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받아서 필요한 변수 생성
    nums, limit = input().split()
    nums, n = list(nums), len(nums)
    limit = int(limit)

    # 1-2. 교환 완료한 숫자판을 담을 result 초기화
    result = []
    change(nums, 0, 0)
    print('#{} {}'.format(tc, max(result)))