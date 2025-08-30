import sys

# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N = int(sys.stdin.readline().rstrip())
schedule = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [0] * (N + 1)

for day in range(N - 1, -1, -1):
    t, p = schedule[day]
    if t + day > N:
        dp[day] = dp[day + 1]
        continue
    dp[day] = max(p + dp[day + t], dp[day + 1])
print(dp[0])