import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
budgets = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())

left = 1
right = M
total = 0
answer = M
while left <= right:
    tmp_total = 0
    middle = (left + right) // 2
    flag = False
    for i in range(N):
        # 만약에 커버가 안되는게 있으면
        if budgets[i] > middle:
            flag = True
            tmp_total += middle
        elif budgets[i] <= middle:
            tmp_total += budgets[i]
    if not flag:
        right = middle - 1
        answer = middle
        continue
    
    if tmp_total > M:
        right = middle - 1
    else:
        left = middle + 1
        answer = middle
    middle = (left + right) // 2
    

print(answer)