import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
city = []

house = []
chiken = []
answer = sys.maxsize

def init():
    global closeCount
    for i in range(N):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(N):
            if row[j] == 1:
                house.append([i, j])
            if row[j] == 2:
                chiken.append([i, j])
        city.append(row)

def findMinDist(select):
    dist = 0
    for h in house:
        curr_dist = N * 2
        for c in select:
            curr_dist = min(curr_dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        dist += curr_dist
    return dist

def backtraking(i, select):
    global answer
    if len(select) == M:
        answer = min(answer, findMinDist(select))
        return
    for i in range(i, len(chiken)):
        select.append(chiken[i])
        backtraking(i + 1, select)
        select.pop()

init()
backtraking(0, [])
print(answer)
