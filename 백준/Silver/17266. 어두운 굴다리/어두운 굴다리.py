import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

position = list(map(int, sys.stdin.readline().rstrip().split()))

def check(mid):
    if position[0] - mid > 0:
        return False
    if position[-1] + mid < N:
        return False
    
    for i in range(M - 1):
        if position[i+1] - position[i] > mid * 2:
            return False
    
    return True

height = N
left = 1
right = N
while left <= right:
    middle = (left + right) // 2
    canLight = check(middle)
    if not canLight:
        left = middle + 1
    if canLight:
        height = middle
        right = middle - 1
print(height)