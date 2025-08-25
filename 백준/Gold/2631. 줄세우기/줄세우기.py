n = int(input())

child = [int(input()) for _ in range(n)]
dp = [1] * (n)
dp[0] = 1
maxLcs = 0
for i in range(1, n):
    for j in range(0, i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(n - max(dp))