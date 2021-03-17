import sys
sys.stdin = open('input.txt')


def start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return [(i, j)]


def escape(road):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    path = []

    while road:
        current = road.pop()
        path.append(current)

        for step in direction:
            next = (current[0] + step[0], current[1] + step[1])
            if next not in path and maze[next[0]][next[1]] == 0:
                road.append(next)
            elif next not in path and maze[next[0]][next[1]] == 3:
                return 1
    return 0


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    road = start()

    print('#{} {}'.format(tc, escape(road)))
