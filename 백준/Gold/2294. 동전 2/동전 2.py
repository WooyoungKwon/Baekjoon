import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

dp = [sys.maxsize] * (K + 1)
dp[0] = 0

for i in range(1, K + 1):
    for coin in coins:
        if coin > i:
            continue
        dp[i] = min(dp[i], dp[i-coin] + 1)
print(dp[K]) if dp[K] != sys.maxsize else print(-1)