import sys
import heapq

n, m, x = map(int, input().split())

square_town = [[] for i in range(n + 1)]
reverse_town = [[] for i in range(n + 1)]

for i in range(m):
    start, end, t = map(int, input().split())
    square_town[start].append([end, t])
    reverse_town[end].append([start, t])

def dijikstra(k, town):
    dist = [sys.maxsize] * (n + 1)
    dist[0] = 0
    dist[k] = 0
    
    pq = []
    heapq.heappush(pq, [0, k])
    
    while pq:
        current = heapq.heappop(pq)
        curr_dist, curr_town = current[0], current[1]
        if dist[curr_town] < curr_dist:
            continue
        
        next_towns = town[curr_town]
        for t in next_towns:
            next_town = t[0]
            next_dist = t[1]
            if dist[next_town] > curr_dist + next_dist:
                dist[next_town] = curr_dist + next_dist
                heapq.heappush(pq, [curr_dist + next_dist, next_town])
    return dist

reserve_result = dijikstra(x, reverse_town)
square_result = dijikstra(x, square_town)

maxTime = 0
for i in range(1, n + 1):
    maxTime = max(maxTime, reserve_result[i] + square_result[i])
print(maxTime)