import sys
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
room = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

cctv_position = []
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            cctv_position.append((i, j, room[i][j]))

cctv_sight = [[], [[0], [1], [2], [3]], [[1, 3], [0, 2]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]], [[0, 1, 2, 3]]]

def sight(x, y, room, direction, num):
    for di in direction:
        nx = x
        ny = y
        while True:
            nx += dx[di]
            ny += dy[di]
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] != 6:
                if 0 < room[nx][ny] < 6:
                    continue
                room[nx][ny] = num
            else:
                break
    return room

def find_zero(room):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == 0:
                cnt += 1
    return cnt

answer = sys.maxsize
def back(cctv_number, room):
    global answer
    if cctv_number == len(cctv_position):
        answer = min(answer, find_zero(room))
        return
    x, y, kind = cctv_position[cctv_number]
    for j in range(len(cctv_sight[kind])):
        copy_room = copy.deepcopy(room)
        sight(x, y, copy_room, cctv_sight[kind][j], 7)
        back(cctv_number + 1, copy_room)
back(0, room)
print(answer)
