def solution(n, times):
    # 2. 이분탐색 함수 생성
    def binary_search(start, end):

        # 2-1. 최소 시간을 start, 최대 시간을 end로 잡고
        while start < end:
            # 2-2. 가운데 값을 기준으로 설정
            mid = (start + end) // 2

            # 2-3. 해당 시간에 몇 명을 입국심사할 수 있는지 확인하기 위해 check 변수 초기화
            check = 0
            # 2-4. 카운터 별 걸리는 시간을 확인하면서
            for time in times:
                # 2-5. 해당 시간에 처리할 수 있는 인원 수를 check에 합산
                check += mid // time

            # 3-1. 가능 인원이 대기 인원보다 적으면 오른쪽(더 큰 시간) 탐색
            if check < n:
                start = mid + 1
            # 3-2. 크거나 같으면 왼쪽 탐색
            # 가능한 경우가 많을 수 있으므로 최솟값 찾기 위해 계속 탐색
            else:
                end = mid

        # 4. start 값 반환
        return start

    # 1. 입국심사에 걸릴 수 있는 최대 시간을 구하고
    maximum = max(times) * n

    return binary_search(1, maximum)

