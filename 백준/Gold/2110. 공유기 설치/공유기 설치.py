import sys

n, c = map(int, sys.stdin.readline().rstrip().split())

homes = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
homes.sort()

start = 1
end = homes[n - 1] - homes[0]
answer = 0
while start <= end:
    dist = (start + end) // 2
    
    lastHome = 0
    count = 1
    for i in range(1, n):
        if homes[i] - homes[lastHome] >= dist:
            lastHome = i
            count += 1
    if count >= c:
        answer = dist
        start = dist + 1
    else:
        end = dist - 1
print(answer)
            
    