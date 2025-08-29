import sys
import math

N = int(sys.stdin.readline().rstrip())

test_center = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

viewer = 0
for center in test_center:
    center -= B
    viewer += 1
    if center > 0:
        viewer += math.ceil(center / C)
print(viewer)
        