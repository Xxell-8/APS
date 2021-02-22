import re


# 1. 정규식 활용
def dart_game_re(dartResult):
    # 1-1. 각 기회당 점수를 담을 result 초기화
    result = [0] * 3
    # 1-2. bonus와 option 점수 저장
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1, '': 1}
    # 1-3. 각 기회의 점수, 보너스, 옵션을 찾아 저장
    scores = re.findall('([0-9]+)([SDT])([*#]*)', dartResult)

    for i in range(3):
        # 2-1. 점수 ** 보너스 * 옵션을 result에 저장하고
        result[i] = int(scores[i][0]) ** bonus[scores[i][1]] * option[scores[i][2]]
        # 2-2. 두번째나 세번째 기회에 스타상이 나오면 직전 점수를 2배로 변경
        if i > 0 and scores[i][2] == '*':
            result[i-1] *= 2

    return sum(result)


# 2. 직접 문자열 계산
def dart_game_self(dartResult):
    # 1-1. 각 기회당 점수를 담을 result 초기화
    result = [0] * 3
    # 1-2. idx 접근을 위해 '10'을 'j'로 변경
    dartResult = dartResult.replace('10', 'j')

    # 1-3. 보너스, 옵션을 저장
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1, '': 1}
    # 1-4. 각 기회의 점수, 보너스, 옵션을 찾아 저장할 scores 초기화
    scores = []

    idx = 0
    while idx < len(dartResult):
        # 2-1. score에 무조건 있는 점수와 보너스 저장
        score = [dartResult[idx], dartResult[idx + 1]]

        # 2-2. 옵션이 있다면 score에 추가하고, idx + 3
        if idx + 2 < len(dartResult) and dartResult[idx + 2] in '*#':
            score.append(dartResult[idx + 2])
            idx += 3
        # 2-3. 없으면 ''를 추가하고 idx + 2
        else:
            score.append('')
            idx += 2
        # 2-4. 각 score를 scores에 추가
        scores.append(score)

    for i in range(3):
        # 3. 'j'는 int 변환이 안되기 때문에 직접 변환
        if scores[i][0] == 'j':
            num = 10
        else:
            num = int(scores[i][0])

        # 4. 각 점수를 계산하고, 스타상이면 직전 점수 2배
        result[i] = num ** bonus[scores[i][1]] * option[scores[i][2]]
        if i > 0 and scores[i][2] == '*':
            result[i-1] *= 2

    return sum(result)


print(dart_game_re('1S2D*3T'))
print(dart_game_re('1D2S#10S'))
print(dart_game_re('1D#2S*3S'))
print()
print(dart_game_self('1S2D*3T'))
print(dart_game_self('1D2S#10S'))
print(dart_game_self('1D#2S*3S'))