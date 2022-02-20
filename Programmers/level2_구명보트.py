def solution(people, limit):
    # 1-1. 구명보트 운영 횟수 answer
    answer = 0
    # 1-2. 사람들을 무게 순으로 정렬하고
    people.sort()
    # 1-3. 양 끝을 각각 ldx, rdx로 지정
    ldx = 0
    rdx = len(people) -1

    # 2. 양 끝점이 교차할 때까지
    while ldx <= rdx:
        # 3-1. 남아있는 가장 가벼운 사람과 무거운 사람을 동시에 옮길 수 있으면 끝점 이동
        if people[ldx] + people[rdx] <= limit:
            ldx += 1
            rdx -= 1
        # 3-2. 불가능하면 무거운 사람만 옮기도록 이동
        else:
            rdx -= 1
        answer += 1

    return answer