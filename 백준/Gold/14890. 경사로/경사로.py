import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split()))
         for _ in range(N)]


# 구현 계획
# 위에서 아래, 왼쪽에서 오른쪽으로 구현한다
# 이동 방향으로 가는 도중
    # i칸과의 차가 1인지. 확인하는 칸의 모든 숫자가 같은지 확인한다.
    # 큰 숫자를 만났을 때: i(나)부터 i - 1.. i - (L - 1)까지 확인한다.
        # 통과했을 경우 i칸에서 i + 1칸으로 이동한다.
    # 작은 숫자를 만났을 때: i + 1(다음 칸)부터 i + L까지 확인한다.
        # 통과했을 경우 i칸에서 i + L 칸으로 이동한다.
# 경사길을 세운 곳은 slope 배열로 표시

def canGo(x, y):
    return 0 <= x < N and 0 <= y < N

# 오른쪽: 0, 아래: 1
dx = [0, 1]
dy = [1, 0]
def canGoRoad(x, y, direction):
    slope = [[False] * N for _ in range(N)]
    while x < N and y < N:
        nx, ny = x + dx[direction], y + dy[direction]
        if nx == N or ny == N:
            return True
        if board[x][y] == board[nx][ny]:
            x, y = nx, ny
            continue
        if abs(board[x][y] - board[nx][ny]) != 1:
            return False
        # 나보다 더 클 때
        if board[x][y] < board[nx][ny]:
            for i in range(L):
                tx = x - (dx[direction] * i)
                ty = y - (dy[direction] * i)
                if canGo(tx, ty):
                    if board[x][y] != board[tx][ty] or slope[tx][ty]:
                        return False
                    else:
                        slope[tx][ty] = True
                else:
                    return False
            x += dx[direction]
            y += dy[direction]
        # 나보다 더 작을 때
        if board[x][y] > board[nx][ny]:
            for i in range(1, L + 1):
                tx = x + (dx[direction] * i)
                ty = y + (dy[direction] * i)
                if canGo(tx, ty):
                    if board[nx][ny] != board[tx][ty] or slope[tx][ty]:
                        return False
                    else:
                        slope[tx][ty] = True
                else:
                    return False
            x += dx[direction] * L
            y += dy[direction] * L

    return True


cnt = 0
for i in range(N):
    if canGoRoad(0, i, 1):
        cnt += 1
    if canGoRoad(i, 0, 0):
        cnt += 1
print(cnt)