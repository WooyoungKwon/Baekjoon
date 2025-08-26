import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
dp = [0] * (K + 1)
stuff = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i in range(N):
    w = stuff[i][0]
    v = stuff[i][1]
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], v + dp[j - w])

print(dp[K])
    
