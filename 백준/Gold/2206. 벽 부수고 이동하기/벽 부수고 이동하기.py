import sys
import copy
from collections import deque
import heapq

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
wall_list = []

n, m = map(int, sys.stdin.readline().rstrip().split())
origin_map = []
for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    for j in range(m):
        if row[j] == "1":
            wall_list.append((i, j))
    origin_map.append(row)

def canGo(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(map):
    q = deque()
    q.append((0, 0, 0, 1))

    # 올바른 초기화 방식
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    
    while q:
        x, y, broken, dist = q.popleft()
        # print(x, y, broken)
        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if canGo(nx, ny):
                if map[nx][ny] == "1":
                    if not visited[nx][ny][1] and broken == 0:
                        visited[nx][ny][1] = True
                        q.append((nx, ny, 1, dist + 1))
                if map[nx][ny] == "0":
                    if not visited[nx][ny][broken]:
                        # print(nx, ny)
                        visited[nx][ny][broken] = True
                        q.append((nx, ny, broken, dist + 1))
                        
    return -1

print(bfs(origin_map))

# print(ans) if ans != sys.maxsize else print(-1)