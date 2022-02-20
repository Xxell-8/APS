# sol 1. 2의 지수 활용
def solution_double(n, a, b):
    count = 0

    while a != b:
        count += 1
        a = (a+1) // 2
        b = (b+1) // 2

    return count

print(solution_double(8, 4, 7))

# sol 2. 재귀 활용
def solution_recursive(n, a, b):
    # 1-1. 길이 n인 리스트를 만들어 a, b 위치에 1 / 나머지 0
    matches = [0] * n
    matches[a-1] = 1
    matches[b-1] = 1

    # 1-2. 라운드 기록
    count = []

    # 2. 각 라운드를 확인할 함수 생성
    def tournament(matches):
        # 3-1. 라운드 시작하면 1 추가
        count.append(1)
        # 3-2. 해당 라운드 승자 기록
        winners = []

        # 4-1. 2명씩 확인
        for idx in range(0, len(matches), 2):
            # 4-2. 둘 다 1이면 종료
            if matches[idx] + matches[idx + 1] == 2:
                return
            # 4-3. 둘 다 0이면 아무나 승자
            elif matches[idx] + matches[idx + 1] == 0:
                winners.append(0)
            # 4-4. 둘 중 하나만 1이면 1이 승자
            else:
                winners.append(1)

        # 5. return으로 함수 종료될 때까지 반복
        tournament(winners)

    tournament(matches)

    return sum(count)


print(solution_recursive(8, 4, 7))