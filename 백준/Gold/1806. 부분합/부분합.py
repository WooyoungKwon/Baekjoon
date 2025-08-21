import sys
from collections import deque

n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

minLen = sys.maxsize
q = deque()

currSum = 0
start = 0
for end in range(n):
    currSum += arr[end]
    while currSum >= s:
        minLen = min(minLen, end - start + 1)
        currSum -= arr[start]
        start += 1

print(minLen if minLen != sys.maxsize else 0)