import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()

# 뱀은 맨왼쪽위, 길이는 1, 방향은 오른쪽
N = int(sys.stdin.readline().rstrip())
N = N + 1
board = [[0] * N for _ in range(N)]
board[1][1] = 1
q.append((1, 1))

head = [1, 1]
tail = [1, 1]

# 사과 위치
K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x][y] = 2


# 뱀의 방향 전환
L = int(sys.stdin.readline().rstrip())
change_direction = [list(sys.stdin.readline().rstrip().split()) for _ in range(L)]

def move(direction):
    global head, tail, board, time
    x, y = q[0]
    head_x = x + dx[direction]
    head_y = y + dy[direction]
    time += 1
    if 1 <= head_x < N and 1 <= head_y < N and board[head_x][head_y] != 1:
        # 머리 이동
        q.appendleft((head_x, head_y))
        # 이동한 곳이 만약 사과가 아니라면
        if board[head_x][head_y] != 2:
            delete_x, delete_y = q.pop()
            board[delete_x][delete_y] = 0
        board[head_x][head_y] = 1
        return True
    else:
        return False

time = 0
direction = 1
turn = 0
while True:
    if move(direction) == False:
        print(time)
        break
    if turn < L and time == int(change_direction[turn][0]):
        if change_direction[turn][1] == "D":
            direction = (direction + 1) % 4
        if change_direction[turn][1] == "L":
            direction = direction - 1
            if direction < 0:
                direction = 3
        turn += 1