import sys

N = int(sys.stdin.readline().rstrip())
cardpack = list(map(int, sys.stdin.readline().rstrip().split()))

# 민규가 카드를 i개 가지기 위해 지불해야 하는 최대값
dp = [0] * (N + 1)
dp[1] = cardpack[0]

for i in range(2, N + 1):
    dp[i] = cardpack[i - 1]
    for j in range(0, i):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[N])
