import sys
import copy
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
virus_start = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(M):
        if 2 == row[j]:
            virus_start.append((i, j))
    board.append(row)
def canGo(x, y, visited, temp_board):
    return 0 <= x < N and 0 <= y < M and not visited[x][y] and temp_board[x][y] == 0
    


def bfs():
    # 바이러스 퍼뜨리고
    temp_board = copy.deepcopy(board)
    visited = [[False] * M for _ in range(N)]
    # 0 개수 세기
    q = deque()
    for virus in virus_start:
        q.append(virus)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if canGo(nx, ny, visited, temp_board):
                temp_board[nx][ny] = 2
                visited[nx][ny] = True
                q.append((nx, ny))
    count = 0
    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == 0:
                count += 1
    return count

answer = 0
def back(wall, start):
    global board, answer
    if wall == 3:
        answer = max(answer, bfs())
        return
    for i in range(start, N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                back(wall + 1, i)
                board[i][j] = 0

back(0, 0)
print(answer)