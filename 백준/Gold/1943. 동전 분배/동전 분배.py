import sys

def solve():
    N = int(sys.stdin.readline().rstrip())
    total = 0
    coins = []
    for _ in range(N):
        coin = list(map(int, sys.stdin.readline().rstrip().split()))
        total += coin[0] * coin[1]
        coins.append(coin)
    if total % 2 == 1:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for price, cnt in coins:
        for i in range(target, price - 1, -1):
            if dp[i - price]:
                for j in range(cnt):
                    if i + price * j <= target:
                        dp[i + price * j] = True
                    else:
                        break
    return dp[target]

# i원을 만드는게 가능한가 ?
for _ in range(3):
    if solve():
        print(1)
    else:
        print(0)