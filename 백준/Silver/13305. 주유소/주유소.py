import sys

N = int(sys.stdin.readline().rstrip())
dist = list(map(int, sys.stdin.readline().rstrip().split()))
cost = list(map(int, sys.stdin.readline().rstrip().split()))

curr = 0
total_cost = 0
while True:
    curr_cost = cost[curr]
    next_dist = 0
    flag = True
    # 다음으로 나보다 더 적은 주유소까지의 거리
    for j in range(curr + 1, N):
        total_cost += (dist[j - 1] * curr_cost)
        if curr_cost > cost[j]:
            curr = j
            flag = False
            break

    if flag or curr == N - 1:
        break

print(total_cost)