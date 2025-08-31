import sys

N = int(sys.stdin.readline().rstrip())
numbers = [0]
a =  list(map(int, sys.stdin.readline().rstrip().split()))
for b in a:
    numbers.append(b)


dp = [1] * (N + 1)
dp[0] = 0

for i in range(1, N  + 1):
    for j in range(i - 1, 0, -1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))