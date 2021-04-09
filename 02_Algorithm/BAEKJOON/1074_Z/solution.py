# 전체 배열 잘라가면서 r, c를 찾는 재귀 함수 생성
def divide(size, row, col):
    # 2-1. result 활용
    global result

    # 2-2. 종료 조건 > row, col이 목표점이 되면 result 값 출력
    if row == r and col == c:
        print(result)
        return

    # 3. 탐색하는 크기(size)에 따라 구분
    # 3-1. size 1일 경우, 범위를 볼 필요 없이 1 더해주고 리턴
    if size == 1:
        result += 1
        return

    # 3-2. 범위 내에 목표점이 없으면 범위만큼 더해주고 리턴
    if not (row <= r < row+size and col <= c < col+size):
        result += size ** 2
        return

    # 4. 사이즈 줄이면서 Z 모양 탐색
    new = size // 2
    divide(new, row, col)
    divide(new, row, col + new)
    divide(new, row + new, col)
    divide(new, row + new, col + new)


# 1-1. input 받고
n, r, c = map(int, input().split())
# 1-2. 결과값 계산할 result 초기화
result = 0

divide(2**n, 0, 0)