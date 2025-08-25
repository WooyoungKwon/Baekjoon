import sys
import heapq

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

busInfo = [[] for _ in range(n + 1)]
for _ in range(m):
    start_city, arrive_city, cost = map(int, sys.stdin.readline().rstrip().split())
    busInfo[start_city].append((cost, arrive_city))

start, end = map(int, sys.stdin.readline().rstrip().split())

pq = []
heapq.heappush(pq, (0, start))

dist = [sys.maxsize] * (n + 1)
while pq:
    data = heapq.heappop(pq)
    curr_cost = data[0]
    curr_bus = data[1]
    if dist[curr_bus] < curr_cost:
        continue

    for nextBusInfo in busInfo[curr_bus]:
        next_cost = nextBusInfo[0] + curr_cost
        next_bus = nextBusInfo[1]
        if next_cost < dist[next_bus]:
            dist[next_bus] = next_cost
            heapq.heappush(pq, (next_cost, next_bus))

print(dist[end])