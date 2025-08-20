import sys
import heapq
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def canGo(x, y, n):
    return 0 <= x < n and 0 <= y < n
        
def simulation(n):
    graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    dist = [[sys.maxsize] * n for _ in range(n)]

    pq = []
    dist[0][0] = graph[0][0]
    heapq.heappush(pq, [graph[0][0], 0, 0])
    
    minDist = sys.maxsize
    
    while pq:
        currDist, x, y = heapq.heappop(pq)
        if x == n - 1 and y == n - 1:
            minDist = min(minDist, currDist)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if canGo(nx, ny, n) and currDist + graph[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = currDist + graph[nx][ny]
                heapq.heappush(pq, [currDist + graph[nx][ny], nx, ny])
    return minDist

num = 1
while(True):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    print(f"Problem {num}: {simulation(n)}")
    num += 1
    