import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

choose = deque()
info = defaultdict(int)
left = 0
right = k - 1
answer = 0
chooseSize = 0
for i in range(left, right + 1):
    choose.append(sushi[i])
    info[sushi[i]] += 1
    if info[sushi[i]] == 1:
        chooseSize += 1
while True:
    if c not in choose:
        answer = max(answer, chooseSize + 1)
    else:
        answer = max(answer, chooseSize)

    if right == k - 2:
        break
    right = (right + 1) % N
    left = (left + 1) % k
    
    tail = choose.popleft()
    choose.append(sushi[right])
    
    info[tail] -= 1
    if info[tail] == 0:
        chooseSize -= 1
        del info[tail]
    info[sushi[right]] += 1
    if info[sushi[right]] == 1:
        chooseSize += 1
        

print(answer)
    