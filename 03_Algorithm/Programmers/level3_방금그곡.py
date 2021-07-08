def solution(m, musicinfos):
    # 1. #이 들어가는 음을 한 글자로 변환해주기
    # 재생 시간과 멜로디를 비교하기 위해 문자열 길이를 활용해야 하기 때문에 음을 다 한 글자로 맞춰주는 작업
    def remove_sharp(code):
        return code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    # 2-1. 네오가 기억하는 멜로디에서 #을 변환해주고
    target = remove_sharp(m)
    # 2-2. 길이를 저장
    length = len(target)

    # 2-3. 기본 변수 초기화
    max_time = 0
    answer = '(None)'

    # 3-1. 방송된 노래들의 정보에서
    for info in musicinfos:
        # 3-2. 각 정보를 변수에 담아주고
        s, e, title, code = info.split(',')
        # 3-3. 재생 시간을 계산
        time = (int(e[:2]) * 60 + int(e[3:])) - (int(s[:2]) * 60 + int(s[3:]))

        # 4-1. 가장 긴 재생 시간보다 현재 곡의 재생 시간이 더 길다면,
        if time > max_time:
            # 4-2. 해당 곡의 멜로디를 변환하고
            music = remove_sharp(code)

            # 4-3. 재생 시간에 따라 문자열 길이 맞추기
            if len(music) > time:
                music = music[:time+1]
            else:
                music *= (time // len(music)) + 1

            # 5-1. 해당 곡의 멜로디에서 네오가 기억하는 멜로디와 매칭되는 문자열 검색
            for idx in range(len(music) - length):
                if music[idx] == target[0]:
                    new = music[idx:idx + length]
                    # 5-2. 매칭되면 해당 곡의 정보를 저장하고, 재생 시간 최댓값 갱신 후 탐색 종료
                    if new == target:
                        answer = title
                        max_time = time
                        break

    return answer
