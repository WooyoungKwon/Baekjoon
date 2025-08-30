import sys

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

max_score = 0

visited = [[False] * M for _ in range(N)]
fuck_x = [[-1, -1, -1], [-1, 0, 1], [1, 1, 1], [-1, 0, 1]]
fuck_y = [[-1, 0, 1], [1, 1, 1], [-1, 0, 1], [-1, -1, -1]]

def dfs(x, y, cnt, score):
    global max_score
    if cnt == 4:
        max_score = max(max_score, score)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, score + board[nx][ny])
            visited[nx][ny] = False

def fuck(x, y):
    global max_score
    for i in range(4):
        can = True
        s = board[x][y]
        for j in range(3):
            nx, ny = x + fuck_x[i][j], y + fuck_y[i][j]
            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                can = False
                break
            s += board[nx][ny]
        if can:
            # print(x, y, s)
            max_score = max(max_score, s)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        fuck(i, j)

print(max_score)