from collections import deque

r, c = map(int, input().split())
miro = [list(input()) for _ in range(r)]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

fq = deque()
fvisited = [[False] * c for _ in range(r)]
jq = deque()
jvisited = [[False] * c for _ in range(r)]

# 지훈이의 초기 위치와 불의 초기 위치 세팅
def init():
    for i in range(r):
        for j in range(c):
            if miro[i][j] == "J":
                jq.append((i, j, 0))
                jvisited[i][j] = True
            elif miro[i][j] == "F":
                fq.append((i, j))
                fvisited[i][j] = True

def canGo(x, y, visited):
    return 0 <= x < r and 0 <= y < c and not visited[x][y] and miro[x][y] != "#"

def canExit(x, y):
    return x == 0 or x == r - 1 or y == 0 or y == c - 1

def bfs():
    while jq:
        fqLen = len(fq)
        for i in range(fqLen):
            fx, fy = fq.popleft()
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if canGo(nfx, nfy, fvisited):
                    fvisited[nfx][nfy] = True
                    miro[nfx][nfy] = "F"
                    fq.append((nfx, nfy))
        # for m in miro:
        #     print(m)
        jqLen = len(jq)
        for i in range(jqLen):
            jx, jy, cnt = jq.popleft()
            if canExit(jx, jy):
                return cnt + 1
            
            for i in range(4):
                njx, njy = jx + dx[i], jy + dy[i]
                if canGo(njx, njy, jvisited):
                    if miro[njx][njy] != "F":
                        if canExit(njx, njy):
                            return cnt + 2
                        jvisited[njx][njy] = True
                        miro[njx][njy] = "J"
                        jq.append((njx, njy, cnt + 1))
    return -1

init()
answer = bfs()
print(answer) if answer != -1 else print("IMPOSSIBLE")