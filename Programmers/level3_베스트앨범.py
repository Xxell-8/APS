def solution(genres, plays):
    # 1-1. answer 초기화
    answer = []
    # 1-2. 장르를 키로 음악 정보를 담을 music 초기화
    music = {}

    # 2-1. 모든 음악을 순회하면서
    for i in range(len(genres)):
        # 2-2. 해당 장르를 생성/조회하고
        music[genres[i]] = music.get(genres[i], [0, []])
        # 2-3. 장르 별 재생 수 계산
        music[genres[i]][0] += plays[i]
        # 2-4. 해당 장르 음악의 재생 수와 고유번호 저장
        music[genres[i]][1].append((plays[i], i))

    # 3-1. 장르별 재생 수를 기준으로 내림차순 정렬
    genre_sort = sorted(music.values(), reverse=True)
    # 3-2. 정렬된 순서대로 순회하며
    for genre in genre_sort:
        items = genre[1]
        # 3-3. 해당 장르 음악이 1개면 answer에 바로 추가
        if len(items) == 1:
            answer.append(items[0][1])
        # 3-4. 여러 개라면,
        else:
            # 3-5. 재생 수 기준 내림차순 정렬 + 고유 번호 오름차순 정렬
            items.sort(key=lambda x: (-x[0], x[1]))
            # 3-6. 해당 장르 음악 2개 answer에 추가
            for i in range(2):
                answer.append(items[i][1])

    return answer