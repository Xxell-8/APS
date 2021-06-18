def solution(tickets):

    # 3. DFS 탐색을 통해 여행 경로 확인
    def dfs(result, airport, visited):
        nonlocal answer

        # 3-1. 항공권 갯수만큼 소진했다면,
        if len(visited) == cnt:
            # 마지막 여행지 추가 후
            result += [airport.pop()]
            # 최종 경로에 추가하고 종료
            answer.append(result)
            return

        # 3-2. 출발지가 더이상 없다면 종료
        if not airport:
            return

        # 4-1. 출발지를 지정하고
        depart = airport.pop()

        # 4-2. 갈 수 있는 여행지가 있다면,
        if airline.get(depart):
            # 4-3. 하나씩 순회하며
            for arrive in airline[depart]:
                info = depart + arrive
                # 4-4. 여행하지 않은 경로라면 추가하고 DFS 탐색
                if info not in visited:
                    dfs(result + [depart], airport + [arrive[:3]], visited + [info])

    # 1-1. 티켓 경로를 저장할 airline 초기화
    airline = {}
    # 1-2. 가능한 공항 경로를 저장할 answer 초기화
    answer = []

    # 1-3. 항공권 소진 확인을 위해 티켓 갯수 저장
    cnt = len(tickets)
    # 1-4. 중복되는 항공권 사용을 위해 고유 번호 지정
    num = 1

    # 2-1. 모든 티켓을 보며
    for ticket in tickets:
        # 2-2. 출발지를 key로 도착지와 고유번호 저장
        airline[ticket[0]] = airline.get(ticket[0], []) + [ticket[1] + str(num)]
        # 2-3. 고유번호 갱신
        num += 1

    # 5-1. ICN에서 출발하여 DFS 탐색 시작
    dfs([], ['ICN'], [])

    # 5-2. 최종 경로를 정렬하여 알파벳 순서가 앞서는 경로 return
    return sorted(answer)[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))