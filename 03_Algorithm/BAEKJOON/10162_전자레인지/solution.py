import sys
sys.stdin = open('input.txt')

# 1-1. input 받기
T = int(input())
# 1-2. A, B, C 버튼에 지정된 시간 지정
buttons = [5 * 60, 1 * 60, 10]

# 2-1. 정확히 시간을 지정할 수 있다면,
if not T % 10:
    # 2-2. 버튼을 누르는 횟수 results 초기화
    results = []
    # 2-3. 남은 시간 저장
    rest = T
    # 2-4. 각 버튼을 큰 순서대로 계산
    for button in buttons:
        # 2-5. 누르는 횟수와 남는 시간 저장
        cnt, rest = divmod(rest, button)
        results.append(str(cnt))
    result = ' '.join(results)
# 3. 정확히 시간을 지정할 수 없으면, -1 반환
else:
    result = -1

print(result)