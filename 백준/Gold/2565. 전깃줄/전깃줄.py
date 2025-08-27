import sys

N = int(sys.stdin.readline().rstrip())
elec = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
elec.sort()

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if elec[i][1] > elec[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))