import sys
import heapq

N = int(sys.stdin.readline().rstrip())


up = []
up_len = 0
down = []
down_len = 0

middle = 0
for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    if middle >= n:
        down_len += 1
        heapq.heappush(down, n * -1)
    else:
        up_len += 1
        heapq.heappush(up, n)


    while down_len > up_len:
        a = heapq.heappop(down)
        heapq.heappush(up, a * -1)
        down_len -= 1
        up_len += 1
        
    if i % 2 == 1 and down_len != up_len:
        while down_len != up_len:
            a = heapq.heappop(up)
            heapq.heappush(down, a * -1)
            up_len -= 1
            down_len += 1

    if up_len == down_len:
        middle = min(down[0] * -1, up[0])
    else:
        middle = up[0]
    print(middle)
