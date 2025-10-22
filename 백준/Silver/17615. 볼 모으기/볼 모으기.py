import sys

input = sys.stdin.readline

N = int(input().rstrip())
balls = list(input().rstrip())


leftRedCnt = 0
preColor = balls[-1]
for i in range(N - 2, -1, -1):
    if balls[i] == "R" and preColor == "B":
        leftRedCnt += 1
    else:
        preColor = balls[i]
        
rightRedCnt = 0
preColor = balls[0]
for i in range(1, N):
    if balls[i] == "R" and preColor == "B":
        rightRedCnt += 1
    else:
        preColor = balls[i]
redCnt = min(leftRedCnt, rightRedCnt)
    
leftBlueCnt = 0
preColor = balls[-1]
for i in range(N - 2, -1, -1):
    if balls[i] == "B" and preColor == "R":
        leftBlueCnt += 1
    else:
        preColor = balls[i]
        
rightBlueCnt = 0
preColor = balls[0]
for i in range(1, N):
    if balls[i] == "B" and preColor == "R":
        rightBlueCnt += 1
    else:
        preColor = balls[i]
blueCnt = min(leftBlueCnt, rightBlueCnt)
print(min(redCnt, blueCnt))