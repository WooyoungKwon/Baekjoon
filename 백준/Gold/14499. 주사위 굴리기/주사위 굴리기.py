import sys


N, M, x, y, K = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 1: 동, 2: 서, 3: 남, 4: 북
commands = list(map(int, sys.stdin.readline().rstrip().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

front = 0
back = 0
left = 0
right = 0
top = 0
under = board[x][y]

def east():
    global front, back, left, right, top, under
    front, back, left, right, top, under = front, back, under, top, left, right

def west():
    global front, back, left, right, top, under
    front, back, left, right, top, under = front, back, top, under, right, left
    

def south():
    global front, back, left, right, top, under
    front, back, left, right, top, under = top, under, left, right, back, front

def north():
    global front, back, left, right, top, under
    front, back, left, right, top, under = under, top, left, right, front, back

def canGo(x, y):
    return 0 <= x < N and 0 <= y < M

def go(x, y):
    global under, board
    if board[x][y] != 0:
        under = board[x][y]
        board[x][y] = 0
    elif board[x][y] == 0:
        board[x][y] = under

for command in commands:
    # print("XY", x, y)
    if command == 1:
        nx = x + dx[1]
        ny = y + dy[1]
        if canGo(nx, ny):
            east()
            go(nx, ny)
            x = nx
            y = ny
            print(top)
    if command == 2:
        nx = x + dx[2]
        ny = y + dy[2]
        if canGo(nx, ny):
            west()
            go(nx, ny)
            x = nx
            y = ny
            print(top)
    if command == 3:
        nx = x + dx[3]
        ny = y + dy[3]
        if canGo(nx, ny):
            south()
            go(nx, ny)
            x = nx
            y = ny
            print(top)
    if command == 4:
        nx = x + dx[4]
        ny = y + dy[4]
        if canGo(nx, ny):
            north()
            go(nx, ny)
            x = nx
            y = ny
            print(top)
