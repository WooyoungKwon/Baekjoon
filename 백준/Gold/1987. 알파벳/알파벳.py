import sys

r, c = map(int, sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

visited = [False] * 26
# A = 65
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

maxCount = 0

def canGo(x, y):
    return 0 <= x < r and 0 <= y < c and not visited[ord(board[x][y]) - 65]

def dfs(x, y, count):
    global maxCount
    maxCount = max(maxCount, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if canGo(nx, ny):
            visited[ord(board[nx][ny]) - 65] = True
            dfs(nx, ny, count + 1)
            visited[ord(board[nx][ny]) - 65] = False
            
visited[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)
print(maxCount)