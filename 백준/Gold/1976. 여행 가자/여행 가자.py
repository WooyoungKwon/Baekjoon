from collections import deque

n = int(input())
m = int(input())

cities = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

def bfs(start, arrive):
    q = deque()
    q.append(start)

    visited = [False] * n
    visited[start] = True

    while q:
        current = q.popleft()
        if current == arrive:
            return True
        for i in range(n):
            if cities[current][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    return False

flag = 0
for i in range(m - 1):
    if not bfs(plan[i] - 1, plan[i + 1] - 1):
        flag = 1
    
if flag == 0:
    print("YES")
else:
    print("NO")

        
    