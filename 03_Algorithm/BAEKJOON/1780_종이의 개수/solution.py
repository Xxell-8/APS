import sys
sys.stdin = open('input.txt')


# 3. 종이 정보를 확인하는 함수 생성
def check_num(row, col, size):
    global result

    # 3-1. 기본 정보값 저장하고
    num = paper[row][col]
    # 3-2. 종이의 정보를 순회하며 하나라도 다르면 false 반환
    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] != num:
                return False

    # 3-3. 모두 같으면 숫자 계산
    if num == -1:
        result[0] += 1
    elif num == 0:
        result[1] += 1
    elif num == 1:
        result[2] += 1
    return True


# 2. 종이 자르는 함수 생성
def divide(row, col, size):
    # 2-1. 종이의 정보가 모두 같지 않으면
    if not check_num(row, col, size):
        # 2-2. 종이의 크기를 9분할(3*3)하고 다시 체크
        new = size // 3
        for i in range(row, row+size, new):
            for j in range(col, col + size, new):
                divide(i, j, new)


# 1. input 받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]

# 4. 종이를 확인하고 자르는 과정 진행
divide(0, 0, N)

# 5. 결과값 출력
for cnt in result:
    print(cnt)