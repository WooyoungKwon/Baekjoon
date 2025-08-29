import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
start_x, start_y, start_direction = map(int, sys.stdin.readline().rstrip().split())

map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clear_count = 0

x, y, direction = start_x, start_y, start_direction

def searchAround():
    global x, y, direction, clear_count
    for i in range(3, -1, -1):
            curr_direction = (direction + i) % 4
            nx = x + dx[curr_direction]
            ny = y + dy[curr_direction]
            if not visited[nx][ny] and map[nx][ny] == 0:
                x = nx
                y = ny
                direction = curr_direction
                return True
while True:
    if not visited[x][y]:
        visited[x][y] = True
        clear_count += 1
         
    # 4칸 중 청소되지 않은 빈 칸이 있다면 이동
    if searchAround():
        continue

    # 4칸 중 청소되지 않은 빈 칸이 없다면 후진
    nx = x + dx[(direction + 2) % 4]
    ny = y + dy[(direction + 2) % 4]
    if map[nx][ny] == 0:
        x = nx
        y = ny
    else:
        break

print(clear_count)