import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
start = int(sys.stdin.readline())

pq = []
heapq.heappush(pq, (0, start))
dist = [sys.maxsize] * (V + 1)
dist[start] = 0

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

while pq:
    data = heapq.heappop(pq)
    curr_dist = data[0]
    curr_v = data[1]
    if dist[curr_v] < curr_dist:
        continue

    for next in graph[curr_v]:
        next_v = next[0]
        next_dist = curr_dist + next[1]
        if dist[next_v] > next_dist:
            dist[next_v] = next_dist
            heapq.heappush(pq, (next_dist, next_v))
    
for i in range(1, V + 1):
    if dist[i] == sys.maxsize:
        print("INF")
    else:
        print(dist[i])
    