def claw_crane(board, moves):
    # 1. 뽑은 인형을 담을 바구니(list) catch 생성
    catch = []
    # 2. 터트려져 사라진 인형의 개수를 셀 answer 변수 초기화
    answer = 0
    ### 각각의 칸은 board[i(행)][j(열)]로 접근 ###
    # 3. 크레인의 움직임(열)을 기준으로
    for j in moves:
        # 4. board의 각각 행을 순서대로 접근
        for i in range(len(board)):
            # 5-1. 접근한 칸에 인형이 있으면
            if board[i][j-1] != 0:
                # 5-2. catch에 인형을 append하고
                catch.append(board[i][j-1])
                # 5-3. 해당 칸을 비우기
                board[i][j-1] = 0
                # 6-1. 잡은 인형이 2개 이상이면
                if len(catch) >= 2:
                    # 6-2. 직전에 잡은 인형과 같은지 확인하고
                    ## 같다면, 2개의 인형 모두 터트리고 answer에 +2
                    if catch[-1] == catch[-2]:
                        del catch[-2:]
                        answer += 2
                # 7. 인형을 잡았으면 다음 크레인 움직임으로 넘어가기
                break
    return answer


claw_crane([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])