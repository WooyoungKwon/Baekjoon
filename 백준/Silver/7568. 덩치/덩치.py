import sys

# 돌의 개수 N을 입력받습니다.
N = int(sys.stdin.readline())
bigBoys = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

moreThanMe = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if bigBoys[i][1] < bigBoys[j][1] and bigBoys[i][0] < bigBoys[j][0]:
            moreThanMe[i] += 1
        elif bigBoys[i][1] > bigBoys[j][1] and bigBoys[i][0] > bigBoys[j][0]:
            moreThanMe[j] += 1

for c in moreThanMe:
    print(c + 1, end=" ")