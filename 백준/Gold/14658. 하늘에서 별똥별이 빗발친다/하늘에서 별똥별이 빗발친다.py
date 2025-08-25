import sys

n, m, l, k = map(int, sys.stdin.readline().rstrip().split())
stars = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(k)]

# starLen = len(stars)

answer = 0
for star_x in stars:
    for star_y in stars:
        x = star_x[0]
        y = star_y[1]
        cnt = 0
        for star_k in stars:
            if x <= star_k[0] <= x + l and y <= star_k[1] <= y + l:
                cnt += 1
        answer = max(answer, cnt)
print(k - answer)

