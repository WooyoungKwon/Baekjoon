import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

a_len = len(a)
b_len = len(b)

dp = [[0] * (a_len + 1) for _ in range(b_len + 1)]

for i in range(1, b_len + 1):
    for j in range(1, a_len + 1):

        if a[j - 1] == b[i - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[b_len][a_len])