def solution(m, n, puddles):

    road = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                road[i][j] = 1
            elif [j, i] in puddles:
                road[i][j] = 0
            else:
                road[i][j] = road[i-1][j] + road[i][j-1]

    return road[n][m] % 1000000007
