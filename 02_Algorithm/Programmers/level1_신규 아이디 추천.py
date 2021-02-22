import re


# 1. 직접 처리
def self_recommend(new_id):
    answer = ''

    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2. 알파벳, 숫자, -, _, . 만 남기기
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in '-_.':
            answer += char

    # 3. 연속된 마침표 하나로 줄이기
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4. 처음과 끝에 위치한 마침표 지우기
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'  # 다음 조건문에서 지워짐
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5. new_id가 빈 문자열이면 a 대입
    if not answer:
        answer = 'a'

    # 6. 길이가 16 이상이면 15개까지 + 마지막이 '.'이면 제거
    if len(answer) >= 16:
        if answer[14] == '.':
            return answer[:14]
        else:
            return answer[:15]

    # 7. 2자 이하면, 마지막 문자를 반복해 길이 3 맞추기
    if len(answer) >= 3:
        return answer
    else:
        while len(answer) < 3:
            answer += answer[-1]
        return answer


# 2. 정규식 활용
def re_recommend(new_id):
    # 1. 대문자를 소문자로 치환
    answer = new_id.lower()
    # 2. 알파벳, 숫자, -, _, . 만 남기기
    answer = re.sub('[^a-z\d\-_.]', '', answer)
    # 3. 연속된 마침표 하나로 줄이기
    answer = re.sub('[.]+', '.', answer)
    # 4. 처음과 끝에 위치한 마침표 지우기
    answer = re.sub('^[.]|[.]$', '', answer)
    # 5. new_id가 빈 문자열이면 a 대입
    # 6. 길이가 16 이상이면 15개까지 + 마지막이 '.'이면 제거
    answer = answer[:15] or 'a'
    answer = re.sub('[.]$', '', answer)
    # 7. 2자 이하면, 마지막 문자를 반복해 길이 3 맞추기
    if len(answer) >= 3:
        return answer
    else:
        while len(answer) < 3:
            answer += answer[-1]
        return answer


print(self_recommend("...!@BaT#*..y.abcdefghijklm"))
print(self_recommend("z-+.^."))
print(self_recommend("=.="))
print(self_recommend("123_.def"))
print(self_recommend("abcdefghijklmn.p"))

print(re_recommend("...!@BaT#*..y.abcdefghijklm"))
print(re_recommend("z-+.^."))
print(re_recommend("=.="))
print(re_recommend("123_.def"))
print(re_recommend("abcdefghijklmn.p"))
