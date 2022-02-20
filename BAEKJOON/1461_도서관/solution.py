import sys
sys.stdin = open('input.txt')


# 4. 책 옮기는 거리 계산 함수 생성
def move_books(array, length):
    global answer

    # 4-1. (예외 처리) 옮길 책이 없으면 종료
    if not length:
        return

    # 4-2. 음수 섹션이면
    if array[0] < 0:
        # M씩 점프하면서 거리 계산
        for idx in range(0, length, M):
            distance = abs(array[idx])
            answer += distance * 2

    # 4-3. 양수 섹션이면
    else:
        # 끝에서부터 -M씩 점프하며 거리 계산
        for idx in range(length-1, -1, -M):
            distance = array[idx]
            answer += distance * 2


# 1. input 받기
N, M = map(int, input().split())
books = list(map(int, input().split()))

# 2-1. 책 위치 정보를 정렬하고
books.sort()
# 2-2. 가장 먼 위치에 있는 책을 마지막에 옮기기
last = max(abs(books[0]), abs(books[-1]))
answer = -last

# 3. 책 위치 정보를 보며 음수/양수로 left/right 나누기
for i in range(N):
    if books[i] > 0:
        left = books[:i]
        right = books[i:]
        break
else:
    left = books[:]
    right = []

# 5. 양쪽 거리 계산 후 answer return
move_books(left, len(left))
move_books(right, len(right))

print(answer)