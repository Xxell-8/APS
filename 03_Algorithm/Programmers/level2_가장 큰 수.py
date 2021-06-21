def solution(numbers):
    # 1. 주어진 숫자 배열의 원소를 string으로 변환
    nums = list(map(str, numbers))
    
    # 2. 원소를 3번 반복해서 크기 비교 (str 숫자 정렬 특성 고려)
    # 원소는 0~1000까지이므로, 한 자릿수 숫자를 고려해 *3 해주기
    nums.sort(key=lambda x: x * 3, reverse=True)

    # 3. 숫자를 합치고, 좌측 0 지우기
    answer = ''.join(nums).lstrip('0')

    # 4. 0이 다 지워진 경우, '0' 리턴
    return answer or '0'