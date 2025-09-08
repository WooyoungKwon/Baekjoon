import sys

# 돌의 개수 N을 입력받습니다.
N, game = sys.stdin.readline().rstrip().split()
N = int(N)
player_count = 0

if game == "Y":
    player_count = 1
elif game == "F":
    player_count = 2
elif game == "O":
    player_count = 3

request = [sys.stdin.readline().rstrip() for _ in range(N)]

played = set()

choose = 0
cnt = 0
for i in range(N):
    if request[i] not in played:
        played.add(request[i])
        choose += 1
    if player_count == choose:
        cnt += 1
        choose = 0
print(cnt)

