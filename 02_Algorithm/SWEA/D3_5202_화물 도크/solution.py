import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1-1. input 받고
    n = int(input())
    apply = [list(map(int, input().split())) for _ in range(n)]
    # 1-2. 사용이 끝나는 시간을 기준으로 정렬
    schedule = sorted(apply, key=lambda x: x[1])

    # 2-1. 필요한 변수 초기화
    fix_end = cnt = 0

    # 2-2. 시작과 끝 시간을 확인하면서
    for start, end in schedule:
        # 2-3. 앞에 예약이 끝나는 시간 이후에 새로운 예약이 시작되면 확정
        if start >= fix_end:
            cnt += 1
            fix_end = end

    print('#{} {}'.format(tc, cnt))